# Ideas
 + GTK application
 + have a little progress bar counting down for 15s max speed + disable update button
 - error window
 - queue statuses n stuff
 - preset statuses
 - status preview
....
# Notes

## TODO
  - be able to save presets from current values
    - its possible to have entries in a dropdown, BUT probably better as a completely new line
    - on save update the config dict, then write to file, refresh the dropdown options etc
  - better data structures for widget stuff ( maybe a widget class or something idk)
    - kinda done, but it would be better to make it like this:
      - every input type has it's own class, and is a child of some generic input thingy
        (yay oop)
  - make the buttons options a thing
  - improve start and end thingy because manual epoch sucks
  - optCon should have a set function... (and optManager should have a set_from_dict function)

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
