#!/usr/bin/env python
from pypresence import Presence
import time, sys

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

from optionsManager import optionsManager
from opCon import opCon
from MyWindow import MyWindow

try:
    f = open("config.yaml")
except:
    raise FileNotFoundError("Missing config.yaml file")

config = load(f.read())
f.close()

print(config)
try:
    RPC = Presence(config["client_id"])
except:
    print("Couldn't find discord running on this machine, exiting.")
    sys.exit(0)

RPC.connect()

win = MyWindow(config, RPC)
win.show_all()
Gtk.main()
