from dataclasses import dataclass
from typing import List, Tuple, Callable
from estrategias_enum import EstrategiasEnum


@dataclass
class Estrategia:
    #Atributos publicos
    monto_apuesta_inicial: int
    unidad_dalambert: int

    #Apostar es un metodo que se asigna al saber que estrategia se va a usar(en el metodo init)
    get_proxima_apuesta: Callable[[bool, int], int]

    #Atributos privados
    __apuestas_pasadas_fibonacci: List[int]
    __cantidad_victorias_paroli: int

    def __init__(self, apuesta_inicial: int, estrategia: str, unidad_dalambert: int = 0):
        if not isinstance(apuesta_inicial, int):
            raise TypeError("La apuesta inicial debe ser un entero")
        if not EstrategiasEnum.has_value(estrategia):
            raise ValueError(
                f"La estrategia debe ser alguno de los siguientes valores {EstrategiasEnum.get_values()}")
        if apuesta_inicial <= 0:
            raise ValueError("No se pueden realizar apuestas iniciales iguales a 0 o menor")
        if not isinstance(unidad_dalambert, int):
            raise TypeError("La unidad:dalambert debe ser entero")

        self.monto_apuesta_inicial = apuesta_inicial
        self.unidad_dalambert = unidad_dalambert
        self.__cantidad_victorias_paroli = 0

        if estrategia == "dalambert":
            self.get_proxima_apuesta = self.__dalambert
        elif estrategia == "fibonacci":
            self.get_proxima_apuesta = self.__fibonacci
        elif estrategia == "martingala":
            self.get_proxima_apuesta = self.__martingala
        elif estrategia == 'paroli':
            self.get_proxima_apuesta = self.__paroli

        self.__apuestas_pasadas_fibonacci = [0, 0, 0]
        print(f"ESTRATEGIA: estas usando '{estrategia}'")

    def __martingala(self, gano_apuesta: bool, cantidad_apostada: int) -> int:
        if not gano_apuesta:
            proxima_apuesta = cantidad_apostada * 2
        else:
            proxima_apuesta = self.monto_apuesta_inicial
        return proxima_apuesta

    def __fibonacci(self, gano_apuesta: bool, cantidad_apostada: int) -> int:
        self.__apuestas_pasadas_fibonacci[2] = self.__apuestas_pasadas_fibonacci[1]
        self.__apuestas_pasadas_fibonacci[1] = self.__apuestas_pasadas_fibonacci[0]
        self.__apuestas_pasadas_fibonacci[0] = cantidad_apostada
        if not gano_apuesta:
            suma_anteriores = self.__apuestas_pasadas_fibonacci[0] + self.__apuestas_pasadas_fibonacci[1]
            proxima_apuesta = max(suma_anteriores, self.monto_apuesta_inicial)
        else:
            proxima_apuesta = max(self.__apuestas_pasadas_fibonacci[2], self.monto_apuesta_inicial)

        return proxima_apuesta

    def __dalambert(self, gano_apuesta: bool, cantidad_apostada: int) -> int:

        if not gano_apuesta:
            proxima_apuesta = cantidad_apostada + self.unidad_dalambert
        else:
            proxima_apuesta = cantidad_apostada - self.unidad_dalambert
        return proxima_apuesta

    def __paroli(self, gano_apuesta: bool, cantidad_apostada: int) -> int:
        print(self.__cantidad_victorias_paroli)
        if not gano_apuesta:
            proxima_apuesta = self.monto_apuesta_inicial
            self.__cantidad_victorias_paroli = 0
        #Se pone como valor maximo el 0 porque se empieza contando del 0
        elif gano_apuesta and self.__cantidad_victorias_paroli <2:
            proxima_apuesta = cantidad_apostada*2
            self.__cantidad_victorias_paroli +=1
        elif gano_apuesta and self.__cantidad_victorias_paroli >=2:
            proxima_apuesta = self.monto_apuesta_inicial
            self.__cantidad_victorias_paroli += 1
        return proxima_apuesta
