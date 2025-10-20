
#! Librerias
import json

class Data:
    @staticmethod
    def cargar_iniciales() -> list:
        try:
            with open('data/iniciales.json', 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            print("Error: No se encontró el archivo iniciales.json")
            return []
        except json.JSONDecodeError:
            print("Error: El archivo JSON no tiene un formato válido")
            return []
    
    @staticmethod
    def cargar_pokemons() -> list:
        try:
            with open('data/pokemons.json', 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            print("Error: No se encontró el archivo pokemons.json")
            return []
        except json.JSONDecodeError:
            print("Error: El archivo JSON no tiene un formato válido")
            return []
        
    @staticmethod
    def cargar_habilidades() -> list:
        try:
            with open('data/habilidades.json', 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            print("Error: No se encontró el archivo habilidades.json")
            return []
        except json.JSONDecodeError:
            print("Error: El archivo JSON no tiene un formato válido")
            return []