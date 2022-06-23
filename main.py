#!/usr/bin/env python
from pypresence import Presence
import time

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.optManager = optionsManager()
        self.init_ui()
        self.render_opts()
        self.timer_countdown = 0

    def render_opts(self):
        i = self.optManager.render_opts(self.pos_grid)
        i+=1
        presetL = Gtk.Label(label="Preset")
        self.pos_grid.attach(presetL, 0, i, 1, 1)
        self.presetCombo = Gtk.ComboBoxText()
        self.presetCombo.set_entry_text_column(0)
        for presetName in config["presets"].keys():
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
        RPC.close()
        Gtk.main_quit()

    def update_status(self, widget):
        print(self.optManager.get_options())
        RPC.update(**self.optManager.get_options())
        self.timer_countdown=600
        GLib.timeout_add(25, self.timer_callback) # start timer, will destroy itself once its reaced 0, due to False return value
        self.updateBtn.set_sensitive(False)

    def use_preset(self, widget):
        selected = self.presetCombo.get_active_text()
        print("Selected preset: {}".format(selected))
        if selected is not None:
            print("Selected preset config: {}".format(config["presets"][selected]))
            current = config["presets"][selected]
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


class opCon(): #container for single option
    def __init__(self, name, type, ttip):
        self.name = name
        self.type = type
        self.label = Gtk.Label(label=self.name)
        self.label.set_tooltip_markup(ttip)
        if self.type=="s" or self.type=="i" or self.type=="l":
            self.entry = Gtk.Entry()
        if self.type=="l":
            self.e2 = Gtk.Entry()
        if self.type=="b":
            self.entry = Gtk.CheckButton(label="Enabled")
    def get(self): # alright, I admit this is a horrible mess by now, I should make seperate classes for the different input types
        if self.type=="s":
            o=self.entry.get_text()
        elif self.type=="l":
            try:
                o=[int(self.entry.get_text()), int(self.e2.get_text())]
            except:
                o=None #something went wrong...
        elif self.type=="b":
            o=self.entry.get_active()
        elif self.type=="i":
            p = self.entry.get_text()
            if len(p)==0:
                return None
            try:
                o = int(self.entry.get_text())
            except ValueError:
                print("{} must be a number".format(self.name))
        if type(o) is str or type(o) is list:
            if len(o) != 0:
                return o
            else:
                return None
        else:
            return o

    def attach_self_row(self, grid, row):
        grid.attach(self.label, 0, row, 1, 1)
        if self.type=="s" or self.type=="i":
            grid.attach(self.entry, 1, row, 3, 1)
        elif self.type=="l":
            grid.attach(self.entry, 1, row, 1, 1)
            grid.attach(self.e2, 2, row, 1, 1)
        elif self.type=="b":
            grid.attach(self.entry, 1, row, 1, 1)

class optionsManager():
    def __init__(self):
        self.opts = [
                    opCon("pid", "i", "the process id of your game"),
                    opCon("state", "s", "the user's current status"),
                    opCon("details", "s", "what the player is currently doing"),
                    opCon("start", "i", "epoch for game start"),
                    opCon("end", "i", "epoch for game end"),
                    opCon("large_image", "s", "name of the uploaded image for the large profile artwork"),
                    opCon("large_text","s", "tooltip for the large image"),
                    opCon("small_image", "s", "name of the uploaded image for the small image"),
                    opCon("small_text", "s", "tooltip for the small image"),
                    opCon("party_id", "s", "id of the player's party, lobby or group"),
                    opCon("party_size", "l", "current size of the player's partym lobby or group, and the max"),
                    opCon("join", "s", "unique hashed string for chat invitations and ask to join"),
                    opCon("spectate", "s", "unique hashed string for spectate button"),
                    opCon("match", "s", "unique hashed string for spectate and join"),
                    #opCon("buttons", "l2"),
                    opCon("instance", "b", "marks the match as a game session with a specific beginning and end")
                    ]
    def render_opts(self, grid):
        for i in range(0, len(self.opts)):
            self.opts[i].attach_self_row(grid, i)
        return i
    def get_options(self):
        params = {}
        for option in self.opts:
            if option.get() is not None:
                params[option.name] = option.get()
        return params
try:
    f = open("config.yaml")
except:
    raise FileNotFoundError("Missing config.yaml file")
config = load(f.read())
f.close()

print(config)

RPC = Presence(config["client_id"])
RPC.connect()

win = MyWindow()
win.show_all()
Gtk.main()
