from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.cards = []  # corrected names of attributes

    @property
    def count(self):
        return len(self.cards)

    def add(self, card: Card):
        if card in [c for c in self.cards]:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)

    def remove(self, card: str):
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        c = self.find(card)
        if c:
            self.cards.remove(c)

    def find(self, name: str):
        return [c for c in self.cards if c.name == name][0]  # maybe try-except if card with this name is not inside
