#!/usr/bin/env python
from pypresence import Presence
import time, sys

from yaml import load, dump, safe_load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

from MyWindow import MyWindow

APPLICATION_DATA = "minimal.yaml"

try:
    f = open(APPLICATION_DATA)
except:
    raise FileNotFoundError("Missing config file ({})".format(APPLICATION_DATA))

config = safe_load(f.read())
f.close()

print(config)
try:
    RPC = Presence(config["client_id"])
except:
    print("Couldn't find discord running on this machine, exiting.")
    sys.exit(0)

RPC.connect()

win = MyWindow(config, RPC, APPLICATION_DATA)
win.show_all()
Gtk.main()
