
#! Librerias
from colorama import Fore, Back, Style # https://pypi.org/project/colorama/
import os

#! Clases
from clases.jugador import Jugador
from clases.data import Data

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
        print(Style.RESET_ALL)

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
        print(Style.RESET_ALL)

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
        print(Style.RESET_ALL)

        os.system('pause')
        os.system('cls')

        self.mostrar_iniciales()

    def seleccionar_color_tipo(self, tipo : str):
        print(Style.BRIGHT, end="")

        if tipo == "Fuego":
            print(Back.RED , end="")
            print(Fore.BLACK, end="")
            return

        if tipo == "Eléctrico":
            print(Back.YELLOW , end="")
            print(Fore.BLACK, end="")
            return

        if tipo == "Planta":
            print(Back.GREEN , end="")
            print(Fore.BLACK, end="")
            return

        if tipo == "Agua":
            print(Back.BLUE , end="")
            print(Fore.BLACK, end="")
            return
        
        if tipo == "Fantasma":
            print(Back.WHITE , end="")
            print(Fore.BLACK, end="")
            return

    def mostrar_iniciales(self):
        
        for pokemon in Data.cargar_iniciales():
            
            self.seleccionar_color_tipo(pokemon["tipo"][0])

            print("-" * 80)
            print("-" * 25 + pokemon["nombre"] + "-" * 5 + "Seleccione con -> [" + str(pokemon["id"]) + "]" + "-" * 20)
            print("-" * 13 + "♥️  PS: " + str(pokemon["puntos_de_salud"]) + " | ", end="")
            print("🛡️  DF: " + str(pokemon["defensa"]) + " | ", end="")
            print("⚔️  DM: " + str(pokemon["ataque"]) + " | ", end="")
            print("💥  PD: " + str(pokemon["poder_de_combate"]) + " | " + "-" * 15)
            print(pokemon["descripción"])
            print("-" * 80)
            print(Style.RESET_ALL)

        self.seleccionar_color_tipo("Fantasma")
        print("-" * 80)
        print("-" * 20 + "Selecciona tu inicial poniendo su número" + "-" * 20)
        print("-" * 80)
        print(Style.RESET_ALL)
        
        self.seleccionar_inicial()
        

    def seleccionar_inicial(self):
        opcion = 0
        while opcion <= 0 or opcion >= 5:
            self.seleccionar_color_tipo("Fantasma")
            opcion = input('Inserta el número a escoger:\t')
            try:
                opcion = int(opcion)
            except Exception:
                print("Seleccione una opción valida")
                opcion = 0
            
        print("Opción seleccionada: " + str(opcion))
        self.jugador.agregar_pokemon(opcion)
        print(Style.RESET_ALL)

        os.system('pause')
        os.system('cls')



if __name__ == "__main__":
    game = App()
