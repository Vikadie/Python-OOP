from project.player.player import Player


class Advanced(Player):
    def __init__(self, username):
        super().__init__(username, 250)
        # self.health = 250
        # self.username = username