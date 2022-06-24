import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

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
