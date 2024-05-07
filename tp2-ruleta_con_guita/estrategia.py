from dataclasses import dataclass
from typing import List, Tuple, Callable
from estrategias_enum import EstrategiasEnum


@dataclass
class Estrategia:


    #Atributos publicos
    monto_apuesta_inicial: int
    unidad_dalambert: int

    #Apostar es un metodo que se asigna al saber que estrategia se va a usar(en el metodo init)
    ruleta = None
    apostar: Callable


    #Atributos privados
    __apuestas_pasadas_fibonacci: List[int]

    def __init__(self, apuesta_inicial: int, estrategia: str, ruleta, unidad_dalambert: int = 0):
        if not isinstance(apuesta_inicial, int):
            raise TypeError("La apuesta inicial debe ser un entero")
        if not EstrategiasEnum.has_value(estrategia):
            raise ValueError(
                f"La estrategia debe ser alguno de los siguientes valores {EstrategiasEnum.show_values()}")
        if apuesta_inicial <= 0:
            raise ValueError("No se pueden realizar apuestas iniciales iguales a 0 o menor")
        if not isinstance(unidad_dalambert, int):
            raise TypeError("La unidad:dalambert debe ser entero")

        self.monto_apuesta_inicial = apuesta_inicial
        self.unidad_dalambert = unidad_dalambert
        if estrategia == "dalambert":
            self.apostar = self.__apostar_dalambert
        elif estrategia == "fibonacci":
            self.apostar = self.__apostar_fibonacci
        elif estrategia == "martingala":
            self.apostar = self.__apostar_martingala
        self.ruleta = ruleta
        self.__apuestas_pasadas_fibonacci = [0, 0, 0]
        print(f"ESTRATEGIA: estas usando {estrategia}")

    def __apostar_martingala(self, cantidad_apostada: int) -> Tuple[int, int]:

        multiplicador_ganancia: int = self.ruleta.apostar()

        ganancia: int = 0

        proxima_apuesta: int = 0
        if not multiplicador_ganancia:
            proxima_apuesta = cantidad_apostada * 2
            ganancia = -cantidad_apostada
        else:
            proxima_apuesta = self.monto_apuesta_inicial
            ganancia = cantidad_apostada * multiplicador_ganancia
        return proxima_apuesta, ganancia

    def __apostar_fibonacci(self, cantidad_apostada: int) -> Tuple[int, int]:

        multiplicador_ganancia: int = self.ruleta.apostar()

        ganancia: int = 0

        proxima_apuesta: int = 0

        self.__apuestas_pasadas_fibonacci[2] = self.__apuestas_pasadas_fibonacci[1]
        self.__apuestas_pasadas_fibonacci[1] = self.__apuestas_pasadas_fibonacci[0]
        self.__apuestas_pasadas_fibonacci[0] = cantidad_apostada
        if not multiplicador_ganancia:
            proxima_apuesta = self.__apuestas_pasadas_fibonacci[0] + self.__apuestas_pasadas_fibonacci[1]
            ganancia = -cantidad_apostada
        else:
            proxima_apuesta = max(self.__apuestas_pasadas_fibonacci[2], self.monto_apuesta_inicial)
            ganancia = cantidad_apostada * multiplicador_ganancia
        return proxima_apuesta, ganancia

    def __apostar_dalambert(self, cantidad_apostada: int) -> Tuple[int, int]:
        global unidad_dalambert
        multiplicador_ganancia: int = self.ruleta.apostar()

        ganancia: int = 0

        proxima_apuesta: int = 0
        if not multiplicador_ganancia:
            proxima_apuesta = cantidad_apostada + self.unidad_dalambert
            ganancia = -cantidad_apostada
        else:
            proxima_apuesta = cantidad_apostada - self.unidad_dalambert
            ganancia = cantidad_apostada * multiplicador_ganancia
        return proxima_apuesta, ganancia
