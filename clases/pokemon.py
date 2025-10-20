
import random

from clases.pokemonBase import PokemonBase
from clases.habilidad import Habilidad
from clases.data import Data
from clases.utils import Utils
from clases.entrenamiento import Entrenamiento

class Pokemon(PokemonBase, Entrenamiento):
    def __init__(self, id_pokemon : int, atrapado : bool = False) -> None:
        super().__init__()
        self.atrapado = atrapado
        self.__crear_pokemon(id_pokemon)
    
    def mostrar_habilidades(self):
        for habilidad in self.habilidades:
            Utils.seleccionar_color_tipo(habilidad.tipo)
            print("=" * 80)
            print("-" * 20 + habilidad.nombre + "-" * 20)
            print("-" * 10 + "🔷  Tipo -> "+ habilidad.tipo + "-" * 10)
            print("-" * 10 + "💥  Potencia -> "+ str(habilidad.potencia) + "-" * 10)
            print("-" * 10 + "🎯  Precisión -> "+ str(habilidad.precision) + "-" * 10)
            print("-" * 10 + "🔋  Coste de PC -> "+ str(habilidad.puntos_de_poder) + "-" * 10)
            print("-" * 10 + "👤  Usable en -> "+ str(habilidad.blanco) + "-" * 10)
            print("-" * 5 + "📝  Descripción:" + "-" * 20)
            print("-" * 5 + habilidad.descripcion + "-" * 20)
            Utils.reset_color()

    def aumentar_nivel(self):
        self.nivel += 100
        if self.nivel >= 100:
            self.evolucionar()
        
    def evolucionar(self):
        Utils.seleccionar_color_tipo("Fuego")
        print("-" * 10 + "Tu Pokemon acaba de evolucionar" + "-" * 10)
        for pokemon in Data.cargar_evoluciones():
            if pokemon["id_pokemon"] == self.id:
                self.nombre = pokemon["nombre"]
                self.tipo = pokemon["tipo"]
                self.descripcion = pokemon["descripción"]
                self.ataque = pokemon["ataque"]
                self.defensa = pokemon["defensa"]
                self.puntos_de_salud = pokemon["puntos_de_salud"]
                self.poder_de_combate = pokemon["poder_de_combate"]
                self.evolucion = pokemon["evolucion"]
                self.nivel = random.randint(1, 6)
                
                Utils.reset_color()
                self.detalles()
                
                return
        
    def __crear_pokemon(self, id : int):
        for pokemon in Data.cargar_pokemons():
            if pokemon["id"] == id:
                self.id = pokemon["id"]
                self.nombre = pokemon["nombre"]
                self.tipo = pokemon["tipo"]
                self.descripcion = pokemon["descripción"]
                self.ataque = pokemon["ataque"]
                self.defensa = pokemon["defensa"]
                self.puntos_de_salud = pokemon["puntos_de_salud"]
                self.poder_de_combate = pokemon["poder_de_combate"]
                self.evolucion = pokemon["evolucion"]
                self.nivel = random.randint(1, 6)
                self.__agregar_habilidades(id)
                return


    def __agregar_habilidades(self, id: int):
        habilidades = []
        for habilidad in Data.cargar_habilidades():
            if habilidad["id_pokemon"] == id:
                habilidades.append(habilidad)
        
        while len(habilidades) > 2:
            index = random.randint(0, len(habilidades) - 1)
            select = habilidades.pop(index)
            nueva_habilidad = Habilidad(
                    select["nombre"], 
                    select["descripción"], 
                    select["tipo"], 
                    select["potencia"], 
                    select["precisión"], 
                    select["puntos_de_poder"], 
                    select["blanco"]
                )
            self.habilidades.append(nueva_habilidad)
        return

    def detalles(self):
        Utils.seleccionar_color_tipo("Fuego")
        print("----- HABLA ASÍ ---------------")
        self.hablar()
        print("----- DETALLES DEL POKEMON ---------------")
        print(f"-----Nombre: {self.nombre} -----")
        print(f"-----Descripcion: {self.descripcion} -----")
        print(f"-----Ataque: {self.ataque} -----")
        print(f"-----Defensa: {self.defensa} -----")
        print(f"-----Puntos de salud: {self.puntos_de_salud} -----")
        print(f"-----Nivel: {self.nivel} -----")
        print(f"-----Evolucion: {self.evolucion} -----")
        print(f"-----Atrapado: {'Si' if self.atrapado else 'No'} -----")
        print("------------------------------------------")
        Utils.reset_color()

    def hablar(self):
        print(f"{self.nombre}! {self.nombre}!")

    def entrenar(self):
        self.ataque += 10
        self.defensa += 10
        self.puntos_de_salud += 10
        self.nivel += 10

        if self.nivel >= 100:
            self.evolucion += 1
            print(f"El pokemon ha evolucionado! Ahora es :{self.nombre}  Evolucion {self.evolucion}")
            self.nivel = 0

    def subir_ataque(self):
        self.ataque += self.boots_ataque
        print(f"Ataque aumentado! Nuevo valor: {self.ataque}")

    def subir_defensa(self):
        self.defensa += self.boots_defensa
        print(f"Defensa aumentada! Nuevo valor: {self.defensa}")

    def subir_puntos_de_salud(self):
        self.puntos_de_salud += self.boots_puntos_de_salud
        print(f"Vida aumentada! Nuevo valor: {self.puntos_de_salud}")

    def actualizar(self):
        self.ataque += self.boots_ataque
        self.defensa += self.boots_defensa
        self.puntos_de_salud += self.boots_puntos_de_salud
        print("Actualizacion completa! ")
        print(f"Ataque: {self.ataque}, Defensa: {self.defensa}, Vida:{self.puntos_de_salud}")


#- Bloque de pruebas: si ejecutas este archivo directamente, usa imports relativos.
if __name__ == "__main__":
    print("Entorno de pruebas")
    pok = Pokemon(1)
    pok.detalles()
    pok.hablar()
    pok.entrenar()
    pok.subirAtaque()
    pok.subirVida()
    pok.actualizar()
    pok.detalles()
    print("-" * 20)
    print(Data.cargar_pokemons())
    print("-" * 20)