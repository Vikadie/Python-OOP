from project.player.player import Player


class Beginner(Player):
    def __init__(self, username):
        super().__init__(username, 50)
        # self.health = 50
        # self.username = username