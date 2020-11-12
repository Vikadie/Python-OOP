from .hero import Hero


class Elf(Hero):
    def __init__(self, username: str, level: int) -> None:
        super().__init__(username, level)
