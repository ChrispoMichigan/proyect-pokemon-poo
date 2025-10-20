
#! Librerias
from colorama import Fore, Back, Style # https://pypi.org/project/colorama/
import os
import random

#! Clases
from clases.jugador import Jugador
from clases.data import Data
from clases.utils import Utils
from clases.enemigo import Enemigo
from clases.combate import Combate

class App:
    def __init__(self):
        self.jugador = Jugador("")
        self.mostrar_menu()

    def mostrar_menu(self):
        for i in range(3):
            print(Back.CYAN + " " * 40 + "\n", end="")
        print(Fore.YELLOW + Back.RED + " " * 10 + "Bienvenido Al Juego" + " " * 11 )
        for i in range(3):
            print(Back.CYAN + " " * 40 + "\n", end="")
        Utils.reset_color

        os.system('pause')
        os.system('cls')
        self.insertar_nombre_jugador()

    def insertar_nombre_jugador(self):
        for i in range(3):
            print(Back.CYAN + " " * 40 + "\n", end="")
        print(Fore.YELLOW + Back.RED + " " * 10 + "Inserta tu nombre: " + " " * 11 )
        for i in range(3):
            print(Back.CYAN + " " * 40 + "\n", end="")
        name = input(Fore.YELLOW + Back.RED + 'Tú nombre aquí:\t')
        Utils.reset_color()

        self.jugador.nombre = name

        os.system('pause')
        os.system('cls')
        self.menu_seleccion()

    def menu_seleccion(self):
        for i in range(3):
            print(Back.CYAN + " " * 40 + "\n", end="")
        print(Fore.YELLOW + Back.RED + " " * 2 + "Parece que aún no tienes un Pokemon" + " " * 3)
        print(" " * 2 + "Selecciona tu inicial a continuación" + " " * 2)
        for i in range(3):
            print(Back.CYAN + " " * 40 + "\n", end="")
        Utils.reset_color()

        os.system('pause')
        os.system('cls')

        self.mostrar_iniciales()

    def mostrar_iniciales(self):
        
        for pokemon in Data.cargar_iniciales():
            
            Utils.seleccionar_color_tipo(pokemon["tipo"][0])

            print("-" * 80)
            print("-" * 25 + pokemon["nombre"] + "-" * 5 + "Seleccione con -> [" + str(pokemon["id"]) + "]" + "-" * 20)
            print("-" * 13 + "♥️  PS: " + str(pokemon["puntos_de_salud"]) + " | ", end="")
            print("🛡️  DF: " + str(pokemon["defensa"]) + " | ", end="")
            print("⚔️  DM: " + str(pokemon["ataque"]) + " | ", end="")
            print("💥  PD: " + str(pokemon["poder_de_combate"]) + " | " + "-" * 15)
            print(pokemon["descripción"])
            print("-" * 80)
            Utils.reset_color()

        Utils.seleccionar_color_tipo("Fantasma")
        print("-" * 80)
        print("-" * 20 + "Selecciona tu inicial poniendo su número" + "-" * 20)
        print("-" * 80)
        Utils.reset_color()
        
        self.seleccionar_inicial()
        

    def seleccionar_inicial(self):
        opcion = 0
        while opcion <= 0 or opcion >= 5:
            Utils.seleccionar_color_tipo("Fantasma")
            opcion = input('Inserta el número a escoger:\t')
            try:
                opcion = int(opcion)
            except Exception:
                print("Seleccione una opción valida")
                opcion = 0
            
        print("Opción seleccionada: " + str(opcion))
        Utils.reset_color()
        
        os.system('pause')
        os.system('cls')

        self.jugador.agregar_pokemon(opcion)
        self.presentar_habilidades_pokemon()
        self.menu_principal()

    def presentar_habilidades_pokemon(self):
        self.jugador.mostrar_habilidades_pokemon(0)

    def menu_principal(self):
        while True:
            opcion = -1
            Utils.seleccionar_color_tipo("Fantasma")
        
            while not opcion in [1, 2, 3]:
                print("-" * 10 + "Opción[1]:Mirar mis pokemons" + "-" * 10 )
                print("-" * 10 + "Opción[2]:Mirar estado de mis pokemons" + "-" * 10 )
                print("-" * 10 + "Opción[3]:Enfrentar Pokemon" + "-" * 10 )
                opcion = input('Inserta el número a escoger:\t')
                try:
                    opcion = int(opcion)
                except Exception:
                    print("Seleccione una opción valida")
                

            if opcion == 1:
                for i in range(len(self.jugador.pokemons)):
                    self.jugador.mostrar_habilidades_pokemon(i)
            if opcion == 2:
                for i in range(len(self.jugador.pokemons)):
                    self.jugador.mostrar_estado_pokemon(i)
            if opcion == 3:
                index = self.jugador.seleccionar_pokemon()
                aleatorio = random.randint(1, len(Data.cargar_pokemons()) - 1)
                enemigo = Enemigo(aleatorio)
                self.iniciar_combate(index, enemigo)

    def iniciar_combate(self, index_pokemon_jugador: int, enemigo : Enemigo):
        """
        Sistema de combate por turnos entre el pokémon del jugador y un enemigo.
        """
        os.system('cls')
        
        pokemon_jugador = self.jugador.pokemons[index_pokemon_jugador]
        pokemon_enemigo = enemigo
        
        vida_jugador = pokemon_jugador.puntos_de_salud
        vida_enemigo = pokemon_enemigo.puntos_de_salud
        turno_jugador = True
        
        Utils.seleccionar_color_tipo("Fantasma")
        print("=" * 60)
        print(" " * 20 + "¡COMBATE POKÉMON!" + " " * 20)
        print("=" * 60)
        Utils.reset_color()
        
        print("\nTU POKÉMON:")
        pokemon_jugador.detalles()
        
        print("\nPOKÉMON ENEMIGO:")
        pokemon_enemigo.detalles()
        
        os.system('pause')
        
        while vida_jugador > 0 and vida_enemigo > 0:
            os.system('cls')
            
            self._mostrar_estado_combate(pokemon_jugador, pokemon_enemigo, vida_jugador, vida_enemigo)
            
            if turno_jugador:
                dano = self._turno_jugador(pokemon_jugador, pokemon_enemigo)
                vida_enemigo = max(0, vida_enemigo - dano)
                
                if vida_enemigo <= 0:
                    break
                    
            else:
                dano = self._turno_enemigo(pokemon_enemigo, pokemon_jugador)
                vida_jugador = max(0, vida_jugador - dano)
                
                if vida_jugador <= 0:
                    break
            
            turno_jugador = not turno_jugador
            os.system('pause')
        
        self._mostrar_resultado_combate(pokemon_jugador, pokemon_enemigo, vida_jugador, vida_enemigo)
    
    def _mostrar_estado_combate(self, pokemon_jugador, pokemon_enemigo, vida_jugador, vida_enemigo):
        """Muestra el estado actual del combate."""
        Utils.seleccionar_color_tipo("Fantasma")
        print("=" * 60)
        print(" " * 20 + "ESTADO DEL COMBATE" + " " * 20)
        print("=" * 60)
        Utils.reset_color()
        
        Utils.seleccionar_color_tipo("Planta")
        print(f"{pokemon_jugador.nombre} (Nivel {pokemon_jugador.nivel})")
        print(f"Vida: {vida_jugador}/{pokemon_jugador.puntos_de_salud}")
        Utils.reset_color()
        
        print(" VS ")
        
        Utils.seleccionar_color_tipo("Fuego")
        print(f"{pokemon_enemigo.nombre} (Nivel {pokemon_enemigo.nivel})")
        print(f"Vida: {vida_enemigo}/{pokemon_enemigo.puntos_de_salud}")
        Utils.reset_color()
        print("-" * 60)
    
    def _turno_jugador(self, pokemon_jugador, pokemon_enemigo):
        """Maneja el turno del jugador."""
        Utils.seleccionar_color_tipo("Planta")
        print(f"\nTurno de {pokemon_jugador.nombre}!")
        Utils.reset_color()
        
        print("\nSelecciona un ataque:")
        for i, habilidad in enumerate(pokemon_jugador.habilidades):
            Utils.seleccionar_color_tipo(habilidad.tipo)
            print(f"{i + 1}. {habilidad.nombre} (Potencia: {habilidad.potencia}, Precisión: {habilidad.precision}%, Tipo: {habilidad.tipo})")
            Utils.reset_color()
        
        while True:
            try:
                opcion = int(input("\nElige tu ataque (número): ")) - 1
                if 0 <= opcion < len(pokemon_jugador.habilidades):
                    habilidad_seleccionada = pokemon_jugador.habilidades[opcion]
                    break
                else:
                    print("Opción inválida. Intenta de nuevo.")
            except ValueError:
                print("Por favor, ingresa un número válido.")
        
        dano = Combate.calcular_dano(
            tipo_usuario=pokemon_jugador.tipo,
            nivel_usuario=pokemon_jugador.nivel,
            tipo_enemigo=pokemon_enemigo.tipo,
            nivel_enemigo=pokemon_enemigo.nivel,
            ataque_usuario=pokemon_jugador.ataque,
            descripcion_ataque=habilidad_seleccionada.nombre,
            defensa_enemigo=pokemon_enemigo.defensa,
            potencia=habilidad_seleccionada.potencia,
            precision=habilidad_seleccionada.precision,
            tipo_ataque=habilidad_seleccionada.tipo
        )
        
        if dano > 0:
            Utils.seleccionar_color_tipo("Fuego")
            print(f"\n{pokemon_enemigo.nombre} recibe {dano} puntos de daño!")
            Utils.reset_color()
        
        return dano
    
    def _turno_enemigo(self, pokemon_enemigo, pokemon_jugador):
        """Maneja el turno del enemigo (IA simple)."""
        Utils.seleccionar_color_tipo("Fuego")
        print(f"\nTurno de {pokemon_enemigo.nombre}!")
        Utils.reset_color()
        
        habilidad_seleccionada = random.choice(pokemon_enemigo.habilidades)
        
        print(f"\n{pokemon_enemigo.nombre} usa {habilidad_seleccionada.nombre}!")
        
        dano = Combate.calcular_dano(
            tipo_usuario=pokemon_enemigo.tipo,
            nivel_usuario=pokemon_enemigo.nivel,
            tipo_enemigo=pokemon_jugador.tipo,
            nivel_enemigo=pokemon_jugador.nivel,
            ataque_usuario=pokemon_enemigo.ataque,
            descripcion_ataque=habilidad_seleccionada.nombre,
            defensa_enemigo=pokemon_jugador.defensa,
            potencia=habilidad_seleccionada.potencia,
            precision=habilidad_seleccionada.precision,
            tipo_ataque=habilidad_seleccionada.tipo
        )
        
        if dano > 0:
            Utils.seleccionar_color_tipo("Fuego")
            print(f"\n{pokemon_jugador.nombre} recibe {dano} puntos de daño!")
            Utils.reset_color()
        
        return dano
    
    def _mostrar_resultado_combate(self, pokemon_jugador, pokemon_enemigo, vida_jugador, vida_enemigo):
        """Muestra el resultado final del combate."""
        os.system('cls')
        
        if vida_enemigo <= 0:
            Utils.seleccionar_color_tipo("Planta")
            print("=" * 60)
            print(" " * 20 + "¡VICTORIA!" + " " * 25)
            print("=" * 60)
            print(f"¡{pokemon_jugador.nombre} ha derrotado a {pokemon_enemigo.nombre}!")
            Utils.reset_color()
            
            self._opcion_atrapar_pokemon(pokemon_enemigo)
            
        else:
            Utils.seleccionar_color_tipo("Fuego")
            print("=" * 60)
            print(" " * 20 + "DERROTA..." + " " * 23)
            print("=" * 60)
            print(f"{pokemon_jugador.nombre} ha sido derrotado por {pokemon_enemigo.nombre}...")
            Utils.reset_color()
        
        os.system('pause')
    
    def _opcion_atrapar_pokemon(self, pokemon_enemigo):
        """Ofrece la opción de atrapar al Pokémon derrotado."""
        Utils.seleccionar_color_tipo("Fantasma")
        print(f"\n¿Quieres intentar atrapar a {pokemon_enemigo.nombre}?")
        print("1. Sí, intentar atraparlo")
        print("2. No, continuar")
        Utils.reset_color()
        
        while True:
            try:
                opcion = int(input("\nElige una opción: "))
                if opcion == 1:
                    if random.random() < 0.5:
                        pokemon_enemigo.atrapado = True
                        self.jugador.pokemons.append(pokemon_enemigo)
                        
                        Utils.seleccionar_color_tipo("Planta")
                        print(f"\n¡Has atrapado a {pokemon_enemigo.nombre}!")
                        print(f"¡{pokemon_enemigo.nombre} se ha unido a tu equipo!")
                        Utils.reset_color()
                    else:
                        Utils.seleccionar_color_tipo("Fuego")
                        print(f"\n¡{pokemon_enemigo.nombre} ha escapado!")
                        Utils.reset_color()
                    break
                elif opcion == 2:
                    print(f"\n{pokemon_enemigo.nombre} se aleja...")
                    break
                else:
                    print("Opción inválida. Intenta de nuevo.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    game = App()
