import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
from optionsManager import optionsManager

class MyWindow(Gtk.Window):
    def __init__(self, config, RPC):
        super().__init__()
        self.optManager = optionsManager()
        self.config = config
        self.timer_countdown = 0
        self.rpc = RPC
        self.init_ui()
        self.render_opts()

    def render_opts(self):
        i = self.optManager.render_opts(self.pos_grid)
        i+=1
        presetL = Gtk.Label(label="Preset")
        self.pos_grid.attach(presetL, 0, i, 1, 1)
        self.presetCombo = Gtk.ComboBoxText()
        self.presetCombo.set_entry_text_column(0)
        for presetName in self.config["presets"].keys():
            self.presetCombo.append_text(presetName)
        self.pos_grid.attach(self.presetCombo, 1, i, 1, 1)
        usePresetBtn = Gtk.Button(label="Use")
        usePresetBtn.connect("clicked", self.use_preset)
        self.pos_grid.attach(usePresetBtn, 2, i, 1, 1)
        i+=1
        aboutBtn = Gtk.Button(label="About")
        #aboutBtn.connect("clicked", self.open_about)
        self.pos_grid.attach(aboutBtn, 0, i, 1, 1)

        self.updateBtn = Gtk.Button(label="Update")
        self.updateBtn.connect("clicked", self.update_status)
        self.pos_grid.attach(self.updateBtn, 1, i, 2, 1)

        quitBtn = Gtk.Button(label="Quit")
        quitBtn.connect("clicked", self.quit)
        self.pos_grid.attach(quitBtn, 3, i, 1, 1)
        i+=1
        self.timeout_bar = Gtk.ProgressBar()
        self.pos_grid.attach(self.timeout_bar, 0, i, 4, 1)

    def init_ui(self):
        self.pos_grid = Gtk.Grid(column_spacing=10,row_spacing=10)
        self.add(self.pos_grid)
        self.set_border_width(10)
        self.set_title("0sleep's Discord RPC")
        self.set_default_size(280, 180)
        self.connect("destroy", self.quit)

    def quit(self, widget):
        self.rpc.close()
        Gtk.main_quit()

    def update_status(self, widget):
        print(self.optManager.get_options())
        self.rpc.update(**self.optManager.get_options())
        self.timer_countdown=600
        GLib.timeout_add(25, self.timer_callback) # start timer, will destroy itself once its reached 0, due to False return value
        self.updateBtn.set_sensitive(False)

    def use_preset(self, widget):
        selected = self.presetCombo.get_active_text()
        print("Selected preset: {}".format(selected))
        if selected is not None:
            print("Selected preset config: {}".format(self.config["presets"][selected]))
            current = self.config["presets"][selected]
            for opt in self.optManager.opts:
                if opt.name in current.keys():
                    if opt.type == "s" or opt.type == "i":
                        opt.entry.set_text(str(current[opt.name]))
                    elif opt.type == "l":
                        opt.entry.set_text(str(current[opt.name][0]))
                        opt.e2.set_text(str(current[opt.name][1]))
                    elif opt.type == "b":
                        opt.entry.set_active(current[opt.name])
    def timer_callback(self):
        if self.timer_countdown > 0:
            self.timer_countdown -= 1
            self.timeout_bar.set_fraction(self.timer_countdown/600)
            return True
        else:
            self.updateBtn.set_sensitive(True)
            return False
