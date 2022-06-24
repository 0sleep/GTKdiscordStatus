import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
from datetime import datetime

class opStrIn():
    def __init__(self, name, ttip):
        self.name = name
        self.label = Gtk.Label(label=self.name)
        self.label.set_tooltip_markup(ttip)
        self.entry = Gtk.Entry()
    def get(self):
        out = self.entry.get_text()
        if out == "":
            return None
        return out
    def set(self, value):
        self.entry.set_text(value)
    def clear(self):
        self.entry.set_text("")
    def attach_self_row(self, grid, row):
        grid.attach(self.label, 0, row, 1, 1)
        grid.attach(self.entry, 1, row, 3, 1)

class opIntIn():
    def __init__(self, name, ttip):
        self.name=name
        self.label=Gtk.Label(label=self.name)
        self.label.set_tooltip_markup(ttip)
        self.entry = Gtk.Entry()
    def get(self):
        out = self.entry.get_text()
        if out == "":
            return None
        try:
            out = int(out)
        except:
            print("Cannot convert {} to int ({})".format(out, self.name))
            return None
        return out
    def set(self, value):
        self.entry.set_text(str(value))
    def clear(self):
        self.entry.set_text("")
    def attach_self_row(self, grid, row):
        grid.attach(self.label, 0, row, 1, 1)
        grid.attach(self.entry, 1, row, 3, 1)

class opBoolIn():
    def __init__(self, name, ttip):
        self.name = name
        self.label = Gtk.Label(label=self.name)
        self.label.set_tooltip_markup(ttip)
        self.entry = Gtk.CheckButton(label="Enabled")
    def get(self):
        out = self.entry.get_active()
        return out
    def set(self, value):
        self.entry.set_active(value)
    def clear(self):
        self.entry.set_active(False)
    def attach_self_row(self, grid, row):
        grid.attach(self.label, 0, row, 1, 1)
        grid.attach(self.entry, 1, row, 1, 1)

class opSelStr():
    def __init__(self, name, ttip, opts):
        self.name = name
        self.opts = opts
        self.label = Gtk.Label(label=self.name)
        self.label.set_tooltip_markup(ttip)
        self.entry = Gtk.Entry()
        self.ddown = Gtk.ComboBoxText()
        for op in self.opts:
            self.ddown.append_text(op)
        self.ddown.connect("changed", self.trigger_on_sel)
    def get(self):
        out = self.entry.get_text()
        if out == "":
            return None
        return out
    def set(self, value):
        self.entry.set_text(value)
    def clear(self):
        self.entry.set_text("")
        self.ddown.set_active(-1)
    def attach_self_row(self, grid, row):
        grid.attach(self.label, 0, row, 1, 1)
        grid.attach(self.entry, 1, row, 1, 1)
        grid.attach(self.ddown, 2, row, 1, 1)
    def trigger_on_sel(self, widget):
        selected = self.ddown.get_active_text()
        self.entry.set_text(selected)

class opList():
    def __init__(self, name, ttip):
        self.name = name
        self.label = Gtk.Label(label=self.name)
        self.label.set_tooltip_markup(ttip)
        self.e1 = Gtk.Entry()
        self.e2 = Gtk.Entry()
    def get(self):
        t1 = self.e1.get_text()
        t2 = self.e2.get_text()
        if t1 == "" or t2 == "":
            return None
        try:
            out = [int(t1), int(t2)]
        except:
            return None
        return out
    def set(self, value):
        self.e1.set_text(str(value[0]))
        self.e2.set_text(str(value[1]))
    def clear(self):
        self.e1.set_text("")
        self.e2.set_text("")
    def attach_self_row(self, grid, row):
        grid.attach(self.label, 0, row, 1, 1)
        grid.attach(self.e1, 1, row, 1, 1)
        grid.attach(self.e2, 2, row, 1, 1)

class opTimeIn():
    def __init__(self, name, ttip, pwindow):
        self.name = name
        self.pwindow = pwindow
        self.label = Gtk.Label(label=self.name)
        self.label.set_tooltip_markup(ttip)
        self.entry = Gtk.Entry()
        self.timeBtn = Gtk.Button(label="Time Picker")
        self.timeBtn.connect("clicked", self.open_picker)
        self.timestamp = None
    def get(self):
        out = self.entry.get_text()
        if out == "":
            return None
        try:
            out = int(out)
        except:
            print("Cannot convert {} to int ({})".format(out, self.name))
            return None
        return out
    def set(self, value):
        self.entry.set_text(str(value))
    def clear(self):
        self.entry.set_text("")
    def attach_self_row(self, grid, row):
        grid.attach(self.label, 0, row, 1, 1)
        grid.attach(self.entry, 1, row, 1, 1)
        grid.attach(self.timeBtn, 2, row, 1, 1)
    def open_picker(self, widget):
        print("open picker")
        self.timestamp = self.get()
        dialog = timePickerDialog(self.pwindow, self.timestamp)
        response = dialog.run()
        print("Received response: {}".format(response))
        if response < 0:
            print("Selector cancelled")
        else:
            self.timestamp = response
            self.set(response)
        dialog.destroy()

class timePickerDialog(Gtk.Dialog):
    def __init__(self, parent, timestamp):
        super().__init__(title="Time Picker", transient_for=parent, flags=0)
        box = self.get_content_area()
        self.pos_grid = Gtk.Grid()
        box.add(self.pos_grid)
        now = datetime.now()

        self.hourBtn = Gtk.SpinButton()
        self.hourBtn.set_orientation(Gtk.Orientation(1))
        self.hourBtn.set_numeric(True)
        self.hourBtn.set_adjustment(Gtk.Adjustment(upper=24, step_increment=1))
        self.hourBtn.set_value(now.hour)
        self.pos_grid.attach(self.hourBtn, 0, 0, 1, 1)

        self.minuteBtn = Gtk.SpinButton()
        self.minuteBtn.set_orientation(Gtk.Orientation(1))
        self.minuteBtn.set_numeric(True)
        self.minuteBtn.set_adjustment(Gtk.Adjustment(upper=60, step_increment=1))
        self.minuteBtn.set_value(now.minute)
        self.pos_grid.attach(self.minuteBtn, 1, 0, 1, 1)

        self.secondBtn = Gtk.SpinButton()
        self.secondBtn.set_orientation(Gtk.Orientation(1))
        self.secondBtn.set_numeric(True)
        self.secondBtn.set_adjustment(Gtk.Adjustment(upper=60, step_increment=1))
        self.secondBtn.set_value(now.minute)
        self.pos_grid.attach(self.secondBtn, 2, 0, 1, 1)

        self.calendar = Gtk.Calendar()
        self.pos_grid.attach(self.calendar, 0, 1, 3, 1)

        self.confirmBtn = Gtk.Button(label="Confirm")
        self.confirmBtn.connect("clicked", self.confirm)
        self.pos_grid.attach(self.confirmBtn, 1, 2, 1, 1)

        self.exitBtn = Gtk.Button(label="Exit")
        self.exitBtn.connect("clicked", self.exit)
        self.pos_grid.attach(self.exitBtn, 2, 2, 1, 1)
        self.show_all()
    def exit(self, widget):
        self.emit("response", -1)
        self.destroy()
    def confirm(self, widget):
        h = self.hourBtn.get_value_as_int()
        m = self.minuteBtn.get_value_as_int()
        s = self.secondBtn.get_value_as_int()
        date = self.calendar.get_date()
        ts = int(datetime(date.year, date.month, date.day, hour=h, minute=m, second=s).timestamp())
        print(ts)
        self.emit("response", ts)
        self.destroy()
