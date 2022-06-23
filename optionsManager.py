from opCon import opCon

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
