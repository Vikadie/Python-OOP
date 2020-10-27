class Guild:

    def __init__(self, name: str):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player in self.list_of_players:
            return f"Player {player.name} is already in the guild."
        else:
            if player.guild != "Unaffiliated":
                return f"Player {player.name} is in another guild."
            else:
                player.guild = self.name
                self.list_of_players.append(player)
                return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        looked_up_player = None
        for pl in self.list_of_players:
            if pl.name == player_name:
                looked_up_player = pl
                break
        else:
            return f"Player {player_name} is not in the guild."
        self.list_of_players.remove(looked_up_player)
        looked_up_player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        info = f"Guild: {self.name}\n"
        for player in self.list_of_players:
            info += f"{player.player_info()}"
        return info
