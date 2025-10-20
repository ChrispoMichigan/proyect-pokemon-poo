
import os

from clases.pokemon import Pokemon
from clases.utils import Utils
class Jugador:
    def __init__(self, nombre : str) -> None:
        self.nombre = nombre
        self.pokemons : list[Pokemon] = []
    
    def agregar_pokemon(self, id : int):
        pokemon = Pokemon(id, True)
        self.pokemons.append(pokemon)

    def mostrar_habilidades_pokemon(self, index : int):
        Utils.seleccionar_color_tipo("Fantasma")
        print("-" * 10 + "Tu Pokemon " + self.pokemons[index].nombre + "-" * 10)
        print("-" * 10 + "Tiene las siguientes habilidades" + "-" * 10)
        self.pokemons[index].mostrar_habilidades()
        Utils.reset_color()

        os.system('pause')
        os.system('cls')

    def mostrar_estado_pokemon(self, index : int):
        Utils.seleccionar_color_tipo("Fantasma")
        print("-" * 10 + "Tu Pokemon " + self.pokemons[index].nombre + "-" * 10)
        print("-" * 10 + "Estado" + "-" * 10)
        self.pokemons[index].detalles()
        Utils.reset_color()

        os.system('pause')
        os.system('cls')

    def seleccionar_pokemon(self) -> int:
        Utils.seleccionar_color_tipo("Fantasma")
        for pokemon in self.pokemons:
            print("-" * 10 + "Selecciona la id: " + str(pokemon.id) + "-" * 10)
            print("-" * 10 + pokemon.nombre + "-" * 10)
        opcion = -1
        while True:
            opcion = input("Inserta la id:\t")
            try:
                opcion = int(opcion)
                break
            except Exception:
                print("Seleccione una opción valida")

        for pokemon in self.pokemons:
            if pokemon.id == opcion:
                return opcion
            
        return -1