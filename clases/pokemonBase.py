from abc import ABC, abstractmethod

class PokemonBase(ABC):
    def __init__(self) -> None:
        self.nombre = "Sin Pokemon"
        self.descripcion = "No descripción"
        self.tipo = []
        self.ataque = 0
        self.defensa = 0
        self.puntos_de_salud = 0
        self.poder_de_combate = 0
        self.nivel = 0
        self.evolucion = 1
        self.atrapado = False
        self.habilidades = []
        self.boots_ataque = 20
        self.boots_defensa = 20
        self.boots_puntos_de_salud = 20

    def imprimir(self):
        print("Desde Pokemon base")

    def subirAtaque(self):
        pass

    def subirDefensa(self):
        pass

    def subirVida(self):
        pass

    @abstractmethod
    def hablar(self):
        pass
    
    @abstractmethod
    def actualizar(self):
        pass

    @abstractmethod
    def detalles(self):
        pass
