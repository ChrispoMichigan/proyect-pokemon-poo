
from abc import ABC, abstractmethod
import os

from clases.utils import Utils
class Entrenamiento(ABC):

    @abstractmethod
    def subir_ataque(self):
        pass

    @abstractmethod
    def subir_defensa(self):
        pass

    @abstractmethod
    def subir_puntos_de_salud(self):
        pass

    def entrenar_pokemon(self, pokemon):
        opcion = -1
        Utils.seleccionar_color_tipo("Fantasma")
    
        while not opcion in [1, 2, 3, 4]:
            print("-" * 10 + "Opción[1]:Aumentar ataque" + "-" * 10 )
            print("-" * 10 + "Opción[2]:Aumentar defensa" + "-" * 10 )
            print("-" * 10 + "Opción[3]:Aumentar salud" + "-" * 10 )
            print("-" * 10 + "Opción[4]:Entrenamiento intensivo (actualiza todo)" + "-" * 10 )
            opcion = input('Inserta el número a escoger:\t')
            try:
                opcion = int(opcion)
            except Exception:
                print("Seleccione una opción valida")

        if opcion == 1:
            pokemon.subir_ataque()

        if opcion == 2:
            pokemon.subir_defensa()

        if opcion == 3:
            pokemon.subir_puntos_de_salud()

        if opcion == 3:
            pokemon.actualizar()

        os.system('pause')
        os.system('cls')