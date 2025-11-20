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
    else:
        print("Entrenamiento aplicado.")
#metodos individuales
  def subirAtaque(self):
      self.ataque += self.BOOST_ATAQUE
      print(f"Ataque aumentada a {self.ataque}")

  def subirDefensa(self):
      self.defensa += self.BOOST_DEFENSA
      print(f"Defensa aumentada a {self.defensa}")

  def subirVida(self):
      self.vida += self.BOOST_VIDA
      print(f"Vida aumentada a {self.vida}")

  def actualizar(self):
      self.ataque += self.BOOST_ATAQUE
      self.defensa += self.BOOST_DEFENSA
      self.vida += self.BOOST_VIDA
      evoluciono = self.subir_nivel(0)
      print(f"Actualizacion completa: ataque, defensa y vida incrementados.")

#subclases especializadas
class Agua(Pokemon):
  def __init__(self, *args, ataque_especial: str = "Hidrobomba", evoluciones_nombres: Opcional[List[str]] = None, **kwargs):
      super().__init__(*args, evoluciones_nombres = evoluciones_nombres or ["Wartortle", "Squirtle", "Blastoise"], **kwargs)
      self.ataque_especial = ataque_especial

  def actualizar(self):
      self.defensa += 10
      print(f"{self.nombre} (Agua) se refresca: +10 defensa.")


class Fuego(Pokemon):
  def __init__(self, *args, ataque_especial: str = "Lanzallamas", evoluciones_nombres: Opcional[List[str]] = None, **kwargs):
      super().__init__(*args, evoluciones_nombres = evoluciones_nombres or ["Charmander", "Charmeleon", "Charizard"], **kwargs)
      self.ataque_especial = ataque_especial

  def actualizar(self):
      self.ataque += 10
      print(f"{self.nombre} (Fuego) se enciende: +10 ataque.") 


class Electrico(Pokemon):
  def __init__(self, *args, ataque_especial: str = "Impactrueno", evoluciones_nombres: Opcional[List[str]] = None, **kwargs):
      super().__init__(*args, evoluciones_nombres = evoluciones_nombres or ["Pichu", "Pikachu", "Raichu"], **kwargs)
      self.ataque_especial = ataque_especial

  def actualizar(self):
      self.vida += 10
      print(f"{self.nombre} (Electtrico) se carga: +10 vida.")


class Hierba(Pokemon):
  def __init__(self, *args, ataque_especial: str = "Rayo Solar", evoluciones_nombres: Opcional[List[str]] = None, **kwargs):
      super().__init__(*args, evoluciones_nombres = evoluciones_nombres or ["Bulsabur", "Ivysaur", "Venusaur"], **kwargs)
      self.ataque_especial = ataque_especial

  def actualizar(self):
      self.ataque += 5
      self.vida += 5
      print(f"{self.nombre} (Hierba) se nutre: +5 ataque, +5 vida.")

#herencia multiple pokemonn con entrenamiento

class PokemonConEntrenamiento(Pokemon, Entrenamiento):
  def subirAtaque(self):
      self.subirAtaque_base() if hasattr(self, "subirAtaque_base") else None
      Pokemon.subirAtaque(self)

  def subirVida(self):
      Pokemon.subirVida(self)

#sistema de combate
  def aplicar dano(atacante_val: int, defensor_def: int, defensor_vida: int) -> Tuple[int, int]:
    #atacando defensa
      resta = atacante_val
      if defensor_def >= resta:
          defensor_def -= resta
      else:
          sobrante = resta - defensor_def
          defensor_def = 0
          defensor_vida -= sobrante
          if defensor_vida < 0
              defensor_vida = 0
      return defensor_def, defensor_vida


#clase app 

class App:
  def __init__(self):
      self.jugador_nombre: str = ""
      self.mi_pokemon: Optional[Pokemon] = None
      self.pokemons_atrapados : List[Pokemon] = []
#enemigos por defecto 2 debiles y 2 fuertes
      self.enemigos: List[Pokemon] = self._crear_enemigos_por_defecto()
      Utils.clear()
      self.bienvenida()
      self.main_loop()

  def bienvenida(self):
      Utils.print_title("Bienvenido a la POKEDEX")
      nombre = input("Ingresa tu nombre: ").strip()
      self.jugador_nombre = nombre if nombre else "Entrenador"
      print(f"\nHola, {self.jugador_nombre}! Aun no tienees Pokemon. Debes elegir uno.")
      Utils.pause()
      Utils.clear()
      self.elegir_inicial()

  def elegir_inicial(self):
      Utils.print_title("Elege tu Pokemon inicial")
      opciones = [
            ("Agua", Agua("Squirtle", "Pokémon tortuga", ataque=20, defensa=30, vida=100, nivel=1, evoluciones_nombres=["Squirtle", "Wartortle", "Blastoise"])),
            ("Fuego", Fuego("Charmander", "Pokémon de fuego", ataque=25, defensa=20, vida=90, nivel=1, evoluciones_nombres=["Charmander", "Charmeleon", "Charizard"])),
            ("Eléctrico", Electrico("Pichu", "Pokémon eléctrico", ataque=18, defensa=18, vida=80, nivel=1, evoluciones_nombres=["Pichu", "Pikachu", "Raichu"])),
            ("Hierba", Hierba("Bulbasaur", "Pokémon planta", ataque=22, defensa=22, vida=95, nivel=1, evoluciones_nombres=["Bulbasaur", "Ivysaur", "Venusaur"]))
        ]
        for idx, (tipo, poke) in enumerate(opciones, strart = 1):
            print(f"{idx}. {tipo} - {poke.nombre} - Ataque {poke.ataque} | Defensa {poke.defensa} | Vida {poke.vida}")
        print("0. Salir")
        while True:
            try:
                sel = int(input("Selecciona el numero del Pokemon que deseas:  "))
                if sel == 0:
                    print("Saliendo...")
                    exit(0)
                if 1 <= sel <= len(opciones):
                    self.mi_pokemon = opciones[sel - 1][1]
                    print(f"\nHas elegido a {self.mi_pokemon.nombre}!")
                    Utils.pause()
                    Utils.clear()
                    self.mi_pokemon.detallesPokemon()
                    Utils.pause()
                    Utils.clear()
                    break
            except ValueError:
                print("Ingresa un numero valido.")


        
      


























  






