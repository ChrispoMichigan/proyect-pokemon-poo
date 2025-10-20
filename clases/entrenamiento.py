
from abc import ABC, abstractmethod
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