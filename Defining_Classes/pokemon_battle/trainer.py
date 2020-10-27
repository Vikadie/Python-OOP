class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemon_lst = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon_lst:
            self.pokemon_lst.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        poke = None
        for pokemon in self.pokemon_lst:
            if pokemon.pokemon_name == pokemon_name:
                poke = pokemon
                break
        if not poke:
            return f"Pokemon is not caught"
        self.pokemon_lst.remove(poke)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        to_return = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon_lst)}\n"
        for pokemon in self.pokemon_lst:
            to_return += f"- {pokemon.pokemon_details()}\n"
        return to_return
