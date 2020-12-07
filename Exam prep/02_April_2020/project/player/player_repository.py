from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.players = []

    @property
    def count(self):
        return len(self.players)

    def add(self, player: Player):
        if player in [p for p in self.players]:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)

    def remove(self, player: str):
        if player == '':
            raise ValueError("Player cannot be an empty string!")
        pl = self.find(player)
        if pl:
            self.players.remove(pl)

    def find(self, username: str):
        return [p for p in self.players if p.username == username][0] # maybe try-except
