import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

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
