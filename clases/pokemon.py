
from pokemonBase import PokemonBase


class Pokemon(PokemonBase):
    def __init__(self) -> None:
        super().__init__()
    

    def hablar(self):
        pass

    def actualizar(self):
        pass

    def detallesPokemon(self):
        pass

#- Bloque de pruebas: si ejecutas este archivo directamente, usa imports relativos.
if __name__ == "__main__":
    print("Entorno de pruebas")

    pok = Pokemon()
    pok.imprimir()
    
    print("Hola ")