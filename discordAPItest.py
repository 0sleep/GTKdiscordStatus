from pypresence import Presence
import time

client_id='988806466318241813'
RPC = Presence(client_id)
RPC.connect()

print(RPC.update(state="Making a GTK application", details="Its gonna be fun :D"))

while True:
    time.sleep(15)
