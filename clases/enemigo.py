
import random

from clases.pokemon import Pokemon
from clases.data import Data
class Enemigo(Pokemon):
    def __init__(self, id_pokemon: int, atrapado: bool = False) -> None:
        super().__init__(id_pokemon, atrapado)