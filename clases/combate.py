
import random
from typing import List 
from clases.utils import Utils

class Combate:
    
    TABLA_EFECTIVIDAD = {
        "Fuego": {
            "supereficaz": ["Planta", "Hielo", "Bicho", "Acero"],
            "resistente": ["Agua", "Roca", "Fuego", "Dragón"],
            "inmune": []
        },
        "Agua": {
            "supereficaz": ["Fuego", "Roca", "Tierra"],
            "resistente": ["Agua", "Planta", "Dragón"],
            "inmune": []
        },
        "Planta": {
            "supereficaz": ["Agua", "Roca", "Tierra"],
            "resistente": ["Fuego", "Planta", "Bicho", "Volador", "Dragón", "Acero"],
            "inmune": []
        },
        "Eléctrico": {
            "supereficaz": ["Agua", "Volador"],
            "resistente": ["Planta", "Eléctrico", "Dragón"],
            "inmune": ["Tierra"]
        },
        "Tierra": {
            "supereficaz": ["Fuego", "Eléctrico", "Veneno", "Roca", "Acero"],
            "resistente": ["Planta", "Bicho"],
            "inmune": ["Volador"]
        },
        "Volador": {
            "supereficaz": ["Planta", "Lucha", "Bicho"],
            "resistente": ["Eléctrico", "Roca", "Acero"],
            "inmune": []
        },
        "Veneno": {
            "supereficaz": ["Planta", "Hada"],
            "resistente": ["Veneno", "Tierra", "Roca", "Fantasma"],
            "inmune": ["Acero"]
        },
        "Normal": {
            "supereficaz": [],
            "resistente": ["Roca", "Acero"],
            "inmune": ["Fantasma"]
        },
        "Lucha": {
            "supereficaz": ["Normal", "Roca", "Acero", "Hielo", "Siniestro"],
            "resistente": ["Volador", "Veneno", "Bicho", "Psíquico", "Hada"],
            "inmune": ["Fantasma"]
        },
        "Psíquico": {
            "supereficaz": ["Lucha", "Veneno"],
            "resistente": ["Psíquico", "Acero"],
            "inmune": ["Siniestro"]
        },
        "Hada": {
            "supereficaz": ["Lucha", "Dragón", "Siniestro"],
            "resistente": ["Fuego", "Veneno", "Acero"],
            "inmune": []
        }
    }

    @staticmethod
    def calcular_dano(
        tipo_usuario: List[str],
        nivel_usuario: int,
        tipo_enemigo: List[str],
        nivel_enemigo: int,
        ataque_usuario: int,
        descripcion_ataque: str,
        defensa_enemigo: int,
        potencia: int,
        precision: int,
        tipo_ataque: str
    ) -> int:
        """
        Calcula el daño infligido basado en los tipos y estadísticas.
        
        Returns:
            int: Daño calculado (entero). Retorna 0 si el ataque falla.
        """
        
        if not Combate._ataque_acierta(precision):
            Utils.seleccionar_color_tipo("Normal")
            print(f"¡{descripcion_ataque} falló!")
            Utils.reset_color()
            return 0
        
        if potencia == 0:
            Utils.seleccionar_color_tipo(tipo_ataque)
            print(f"¡{descripcion_ataque} fue usado!")
            Utils.reset_color()
            return 0
        
        multiplicador_efectividad = Combate._calcular_efectividad(tipo_ataque, tipo_enemigo)
        
        stab = 1.5 if tipo_ataque in tipo_usuario else 1.0
        

        nivel_factor = (2 * nivel_usuario + 10) / 250
        
        factor_defensa_enemigo = 1.0 + (max(0, nivel_enemigo - 1) * 0.1)
        defensa_potenciada = defensa_enemigo * factor_defensa_enemigo
        
        ataque_defensa_ratio = ataque_usuario / max(defensa_potenciada, 1)  # Evitar división por 0

        factor_aleatorio = random.uniform(0.85, 1.0)
        
        dano_base = ((nivel_factor * ataque_defensa_ratio * potencia) + 2)
        dano_final = dano_base * stab * multiplicador_efectividad * factor_aleatorio
        
        dano_final = max(1, int(dano_final))
        
        Combate._mostrar_efectividad(multiplicador_efectividad, tipo_ataque, descripcion_ataque)
        
        return dano_final
    
    @staticmethod
    def _ataque_acierta(precision: int) -> bool:
        return random.randint(1, 100) <= precision
    
    @staticmethod
    def _calcular_efectividad(tipo_ataque: str, tipos_enemigo: List[str]) -> float:

        multiplicador_total = 1.0
        
        if tipo_ataque not in Combate.TABLA_EFECTIVIDAD:
            return multiplicador_total
        
        efectividad = Combate.TABLA_EFECTIVIDAD[tipo_ataque]
        
        for tipo_defensor in tipos_enemigo:
            if tipo_defensor in efectividad["inmune"]:
                return 0.0  # Inmune anula todo
            elif tipo_defensor in efectividad["supereficaz"]:
                multiplicador_total *= 2.0
            elif tipo_defensor in efectividad["resistente"]:
                multiplicador_total *= 0.5
        
        return multiplicador_total
    
    @staticmethod
    def _mostrar_efectividad(multiplicador: float, tipo_ataque: str, descripcion_ataque: str):
        Utils.seleccionar_color_tipo(tipo_ataque)
        
        if multiplicador == 0.0:
            print(f"¡{descripcion_ataque} no afecta al enemigo!")
        elif multiplicador > 1.0:
            print(f"¡{descripcion_ataque} es supereficaz!")
        elif multiplicador < 1.0:
            print(f"¡{descripcion_ataque} no es muy eficaz!")
        else:
            print(f"¡{descripcion_ataque} conecta!")
        
        Utils.reset_color()