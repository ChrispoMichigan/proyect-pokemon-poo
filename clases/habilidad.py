
class Habilidad:
    def __init__(self, nombre, descripción, tipo, potencia, precision, puntos_de_poder, blanco) -> None:
        self.nombre : str = nombre
        self.descripcion : str = descripción
        self.tipo : str = tipo
        self.potencia : int = potencia
        self.precision : int = precision
        self.puntos_de_poder : int = puntos_de_poder
        self.blanco : str = blanco