from project.player.player import Player


class BattleField:
    def fight(self, attacker: Player, enemy: Player):

        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        for player in (attacker, enemy):
            if player.__class__.__name__ == 'Beginner':
                player.health += 40
                for card in player.card_repository.cards:
                    card.damage_points += 30

            bonus = sum([card.health_points for card in player.card_repository.cards])
            player.health += bonus

        damage_points_attacker = sum([card.damage_points for card in attacker.card_repository.cards])
        enemy.take_damage(damage_points_attacker)

        damage_points_enemy = sum([card.damage_points for card in enemy.card_repository.cards])
        attacker.take_damage(damage_points_enemy)