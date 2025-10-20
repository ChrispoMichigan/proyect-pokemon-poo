
from clases.pokemonBase import PokemonBase

from clases.data import Data

class Pokemon(PokemonBase):
    def __init__(self, id_pokemon : int) -> None:
        super().__init__()

        self.__crear_pokemon(id_pokemon)

    def __crear_pokemon(self, id : int):
        for pokemon in Data.cargar_pokemons():
            if pokemon["id"] == id:
                self.nombre = pokemon["nombre"]
                self.tipo = pokemon["tipo"]
                self.descripcion = pokemon["descripción"]
                self.ataque = pokemon["ataque"]
                self.defensa = pokemon["defensa"]
                self.puntos_de_salud = pokemon["puntos_de_salud"]
                self.poder_de_combate = pokemon["poder_de_combate"]
                self.evolucion = pokemon["evolucion"]
                self.__agregar_habilidades(id)
                return


    def __agregar_habilidades(self, id: int):
        habilidades = []
        for habilidad in Data.cargar_habilidades():
            if habilidad["id_pokemon"] == id:
                habilidades.append(habilidad)
        print(habilidad)

    def detalles(self):
        print("----- DETALLES DEL POKEMON -----")
        print(f"Nombre: {self.nombre}")
        print(f"Descripcion: {self.descripcion}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self.nivel}")
        print(f"Evolucion: {self.evolucion}")
        print(f"Atrapado: {'Si' if self.atrapado else 'No'}")
        print("--------------------------------")

    def hablar(self):
        print(f"{self.nombre}! {self.nombre}!")

    def entrenar(self):
        self.ataque += 10
        self.defensa += 10
        self.vida += 10
        self.nivel += 10

        if self.nivel >= 100:
            self.evolucion += 1
            print(f"El pokemon ha evolucionado! Ahora es :{self.nombre}  Evolucion {self.evolucion}")
            self.nivel = 0

    def subirAtaque(self):
        self.ataque += self.boots_ataque
        print(f"Ataque aumentado! Nuevo valor: {self.ataque}")

    def subirDesensa(self):
        self.defensa += self.boots_defensa
        print(f"Defensa aumentada! Nuevo valor: {self.defensa}")

    def subirVida(self):
        self.vida += self.boots_puntos_de_salud
        print(f"Vida aumentada! Nuevo valor: {self.vida}")

    def actualizar(self):
        self.ataque += self.boots_ataque
        self.defensa += self.boots_defensa
        self.vida += self.boots_puntos_de_salud
        print("Actualizacion completa! ")
        print(f"Ataque: {self.ataque}, Defensa: {self.defensa}, Vida:{self.vida}")


#- Bloque de pruebas: si ejecutas este archivo directamente, usa imports relativos.
if __name__ == "__main__":
    print("Entorno de pruebas")
    pok = Pokemon(1)
    pok.detalles()
    pok.hablar()
    pok.entrenar()
    pok.subirAtaque()
    pok.subirDefensa()
    pok.subirVida()
    pok.actualizar()
    pok.detalles()
    print("-" * 20)
    print(Data.cargar_pokemons())
    print("-" * 20)