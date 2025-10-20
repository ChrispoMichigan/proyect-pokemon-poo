
from colorama import Fore, Back, Style # https://pypi.org/project/colorama/

class Utils:
    @staticmethod
    def seleccionar_color_tipo(tipo: str):
        
        """
        Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
        Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
        """

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
        
        if tipo == "Normal":
            print(Back.CYAN , end="")
            print(Fore.WHITE, end="")
            return
        
        if tipo == "Veneno":
            print(Back.MAGENTA , end="")
            print(Fore.WHITE, end="")
            return
        
        if tipo == "Psíquico":
            print(Back.BLACK , end="")
            print(Fore.WHITE, end="")
            return
        
        

    @staticmethod 
    def reset_color():
        print(Style.RESET_ALL)