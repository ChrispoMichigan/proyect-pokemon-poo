from __future__ import annotations
import random 
from abc import ABC, abstractmethod 
from typing import List, Optional, Tuple

class Utils:
  @staticmethod 
  def clear():
    import os 
    os.system("cls" if os.name == "nt" else "clear")

  @staticmethod
  def pause():
    try:
      input("\nPresiona Enter para continuar..")
    except Exception:
      pass

  @staticmethod
  def print_title(t: str):
      print("=" * 60 )
      print(t.center(60))
      print("=" * 60)


class PokemonBase(ABC):
  def __init__(self,
      nombre: str = "Sin Pokemon"
      descripcion: str = "No descripcion",
      ataque: int = 0,
      defensa: int = 0,
      vida: int = 0,
      nivel: int = 1,
      evolucion: int 1,
      atrapado: bool = False):

      self.nombre: str = nombre
      self.descripcion: str = descripcion
      self.ataque: int = max(0, int(ataque))
      self.defensa: int = max(0, int(defensa))
      self.vida: int = max(0, int(vida))
      self.nivel: int = max(1, int(nivel))
      self.evolucion: int = max(1, int(evolucion))

      if self.evolucion > 3:
          self.evolucion = 3
      self.atrapadp: bool = atrapado

  @abstractmethod
  def hablar(self):
      raise NotImplementedError

  @abstractmethod
  def actualizar(self):
      raise NotImplementedError

  @abstractmethod
  def detallesPokemon(self):
      raise NotImplementedError

  def subir_nivel(self, inc: int = 10, reiniciar_on_evol: bool = True):
      self.nivel += inc
      if self.nivel >= 100:

        if self.evolucion < 3:
            self.evolucion += 1
            self.nivel = 0
            return True 
        else:
            self.nivel = 0
      return False


#Entrenamiento abstracto
class Entrenamiento(ABC):
  @abstractmethod
  def subirAtaque(self):
      raise NotImplementedError

  
  @abstractmethod
  def subirDefensa(self):
      raise NotImplementedError

  @abstractmethod
  def subirVida(self):
      raise NotImplementedError
        
#Clase Pokemon

class Pokemon(PokemonBase):
  BOOST_ATAQUE = 20 
  BOOST_DEFENSA = 20
  BOOST_VIDA = 20

  def __init__(self,
      nombre: str = "Sin Pokemon"
      descripcion: str = "No descripcion",
      ataque: int = 0,
      defensa: int = 0,
      vida: int = 0,
      nivel: int = 1,
      evolucion: int 1,
      atrapado: bool = False):
      evoluciones_nombres: Optional[List[str]] = None
      ):
      super().__init__(nombre, descripcion, ataque, defensa, vida, nivel, evolucion, atrapado)

      if evoluciones_nombres:
          self.evoluciones_nombres = evoluciones_nombres[:3]
      else:
          self.evoluciones_nombres = [self.nombre]


      if 1 <= self.evolucion <= len(self.evoluciones_nombres):
          self.nombre = self.evoluciones_nombres[self.evolucion - 1 ]

  def detallesPokemon(self):
      Utils.print_title("DETALLES DEL POKEMON")
      print(f"Nombre         : {self.nombre}")
      print(f"Descripcion    : {self.descripcion}")    
      print(f"Ataque         : {self.ataque}")    
      print(f"Defensa        : {self.defensa}")
      print(f"Vida           : {self.vida}")
      print(f"Nivel          : {self.nivel}")
      print(f"Evolucion      : {self.evolucion}")
      print(f"Atrapado       : {self.atrapado}")

def hablar(self):
    print(f"{self.nombre}! {self.nombre}!")

def entrenar(self):

    self.ataque += 10
    self.defensa += 10
    self.vida += 10
    evoluciono = self.subir_nivel(10)
    if evoluciono:
        old = self.nombre

        idx = min(self.evolucion - 1, len.evoluciones_nombres) - 1)
        self.nombre = self.evoluciones_nombres[idx]
        print(f"El Pokemon ha evolucionado!! Ahora es {self.nombre}")



















