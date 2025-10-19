
from pokemonBase import PokemonBase


class Pokemon(PokemonBase):
    def __init__(self, nombre = "Pikachu", descripcion = "Un pokemon electrico"):
        super().__init__()
        self.nombre = nombre
        self.descripcion = descripcion
        self.ataque = 50
        self.defensa = 40
        self.vida = 60
        self.nivel = 10
        self.evolucion = 0
        self.atrapado = False

        self.boots_ataque = 20
        self.boots_defensa = 20
        self.boots_vida = 20

    def detalles(self):
        print("----- DETALLES DEL POKEMON -----")
        print(f"Nombre: {self.nombre}")
        print(f"Descripcion: {self.descripcion}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self.nivel}")
        print(f"Evolucion: {self.evolucion}")
        print(f"Atrapado: {'Si' if self.atrpado else 'No'}")
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
        self.vida += self.boots_vida
        print("Vida aumentada! Nuevo valor: {self.vida}")

    def alctualizar(self):
        self.ataque += self.boots_ataque
        self.defensa += self.boots_defensa
        self.vida += self.boots_vida
        print("Actualizacion completa! ")
        print(f"Ataque: {self.ataque}, Defensa: {self.defensa}, Vida:{self.vida}")


#- Bloque de pruebas: si ejecutas este archivo directamente, usa imports relativos.
if __name__ == "__main__":
    print("Entorno de pruebas")
    pok = Pokemon()
    pok.detalles()
    pok.hablar()
    pok.entrenar()
    pok.subirAtaque()
    pok.subirDefensa()
    pok.subirVida()
    pok.actualizar()
    pok.detalles()
