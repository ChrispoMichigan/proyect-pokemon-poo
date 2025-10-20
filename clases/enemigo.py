from clases.pokemon import Pokemon


class Enemigo(Pokemon):
    def __init__(self, id_pokemon: int, atrapado: bool = False) -> None:
        super().__init__(id_pokemon, atrapado)

    def __generar_enemigo(self):
        self.__crear_pokemon()