from opCon import *

class optionsManager():
    def __init__(self, config, pwindow):
        self.config = config
        self.pwindow = pwindow
        self.opts = [
                    opIntIn("pid", "the process id of your game"),
                    opStrIn("state", "the user's current status"),
                    opStrIn("details", "what the player is currently doing"),
                    opTimeIn("start", "epoch for game start", self.pwindow),
                    opTimeIn("end", "epoch for game end", self.pwindow),
                    opSelStr("large_image", "name of the uploaded image for the large profile artwork", self.config["images"]),
                    opStrIn("large_text", "tooltip for the large image"),
                    opSelStr("small_image", "name of the uploaded image for the small image", self.config["images"]),
                    opStrIn("small_text", "tooltip for the small image"),
                    opStrIn("party_id", "id of the player's party, lobby or group"),
                    opList("party_size", "current size of the player's partym lobby or group, and the max"),
                    opStrIn("join", "unique hashed string for chat invitations and ask to join"),
                    opStrIn("spectate", "unique hashed string for spectate button"),
                    opStrIn("match", "unique hashed string for spectate and join"),
                    #opCon("buttons", "l2"), # TODO implement some sort of multi disappearing thing for this
                    opBoolIn("instance", "marks the match as a game session with a specific beginning and end")
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
    def set_options(self, selected):
        selConf = self.config["presets"][selected]
        setOpts = selConf.keys()
        for opt in self.opts:
            if opt.name in setOpts:
                opt.set(selConf[opt.name])
    def clear(self):
        for opt in self.opts:
            opt.clear()
