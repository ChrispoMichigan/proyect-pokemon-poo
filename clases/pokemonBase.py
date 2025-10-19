from abc import ABC, abstractmethod

class PokemonBase(ABC):
    def __init__(self) -> None:
        self.nombre = "Sin Pokemon"
        self.descripcion = "No descripción"
        self.ataque = 0
        self.defensa = 0
        self.vida = 0
        self.nivel = 0
        self.evolucion = 1
        self.atrapado = False

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
    def detallesPokemon(self):
        pass
