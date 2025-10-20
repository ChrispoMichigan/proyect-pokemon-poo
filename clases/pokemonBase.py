from abc import ABC, abstractmethod

from clases.habilidad import Habilidad
class PokemonBase(ABC):
    def __init__(self) -> None:
        self.id : int = -1
        self.nombre : str = "Sin Pokemon"
        self.descripcion : str = "No descripción"
        self.tipo : list[str] = []
        self.ataque : int = 0
        self.defensa : int = 0
        self.puntos_de_salud : int = 0
        self.poder_de_combate : int = 0
        self.nivel : int = 0
        self.evolucion : int = 1
        self.atrapado : bool = False
        self.habilidades: list[Habilidad] = []
        self.boots_ataque : int = 20
        self.boots_defensa : int = 20
        self.boots_puntos_de_salud : int = 20

    def imprimir(self):
        print("Desde Pokemon base")

    @abstractmethod
    def hablar(self):
        pass
    
    @abstractmethod
    def actualizar(self):
        pass

    @abstractmethod
    def detalles(self):
        pass
