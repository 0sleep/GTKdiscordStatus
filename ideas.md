# Ideas
 + GTK application
 + have a little progress bar counting down for 15s max speed + disable update button
 - error window
 - queue statuses n stuff
 + preset statuses
 - status preview
....
# Notes

## TODO
  - make the buttons options a thing (for "buttons")
  - in in vs str in differentiate
  - make yaml load safely
  - improve main menu layout (make 6 wide!)
  - add about
  - add application logo thing
  - fix quit problem
  Traceback (most recent call last):
  File "/home/rootuser/Documents/Programming/GTKdiscordStatus/MyWindow.py", line 73, in quit
    self.rpc.close()
  File "/usr/local/lib/python3.8/dist-packages/pypresence/presence.py", line 48, in close
    self.send_data(2, {'v': 1, 'client_id': self.client_id})
  File "/usr/local/lib/python3.8/dist-packages/pypresence/baseclient.py", line 96, in send_data
    assert self.sock_writer is not None, "You must connect your client before sending events!"
AssertionError: You must connect your client before sending events!
  - finally: add comments, remove debug print, README etc.

## TMP
self.opts = [
        opCon("pid", "i"),
        opCon("state", "s"),
        opCon("details", "s"),
        opCon("start", "i"),
        opCon("end", "i"),
        opCon("large_image", "s"),
        opCon("large_text","s"),
        opCon("small_image", "s"),
        opCon("small_text", "s"),
        opCon("party_id", "s"),
        opCon("party_size", "l"),
        opCon("join", "s"),
        opCon("spectate", "s"),
        opCon("match", "s"),
        #opCon("buttons", "l2"),
        opCon("instance", "b")
        ]
