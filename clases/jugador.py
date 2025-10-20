
from clases.pokemon import Pokemon

class Jugador:
    def __init__(self, nombre : str) -> None:
        self.nombre = nombre
        self.pokemons = []
    
    def agregar_pokemon(self, id : int):
        pass