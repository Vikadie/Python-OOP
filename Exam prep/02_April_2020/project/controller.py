from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()  # corrected mistake

    def add_player(self, type: str, username: str):  # renamed type to type
        player = Beginner(username) if type == 'Beginner' else Advanced(username)
        self.player_repository.add(player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type: str, name: str):  # renamed type to type
        card = MagicCard(name) if type == 'Magic' else TrapCard(name)
        self.card_repository.add(card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username: str, card_name: str):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        battlefield = BattleField()
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        battlefield.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        report = ''
        for player in self.player_repository.players:
            report += f'Username: {player.username} - Health: {player.health} - Cards {player.card_repository.count}\n'
            for card in player.card_repository.cards:
                report += f'### Card: {card.name} - Damage: {card.damage_points}\n'
        return report
