from dataclasses import dataclass
from random import randint
from typing import Set, Callable, Union, List, Dict


@dataclass
class Ruleta:
    numeros_rojos: Set[int]
    numeros_negros: Set[int]
    numeros_salidos:List
    contador_tiradas:int
    historico_promedios:List[int]

    __apuesta_maxima:int
    __forma_apuesta_elegida: Callable


    def __init__(self, valor_apostado: str | int, apuesta_maxima:int):

        self.set_forma_apuesta(valor_apostado)
        self.set_apuesta_maxima(apuesta_maxima)
        self.numeros_salidos = [0 for i in range(0,37)]
        self.historico_promedios = []
        self.contador_tiradas = 0
        self.numeros_rojos = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
        self.numeros_negros = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

        print(f"RULETA: Estas apostando al '{valor_apostado}'")
    def set_apuesta_maxima(self,apuesta_maxima:int ):
        if not isinstance(apuesta_maxima,int ):
            raise TypeError("No se ingreso una apuesta maxima entera")
        if apuesta_maxima <=0:
            raise ValueError("Ingrese una apuesta maxima valida")
        self.__apuesta_maxima = apuesta_maxima
    def set_forma_apuesta(self, valor_apostado: str| int):
        if not (isinstance(valor_apostado, int) or isinstance(valor_apostado, str)):
            raise TypeError("La apuesta debe ser un entero o una string")
        if not (valor_apostado in [i for i in range(0, 37)] or valor_apostado in ['rojo', 'negro', 'par', 'impar']):
            raise ValueError(
                "No ingreso una apuesta valida, debe ser un valor entre 0 y 36 o bien rojo, negro, par o impar")
        if valor_apostado in [i for i in range(0, 37)]:
            self.__forma_apuesta_elegida = self.__apostar_numero(valor_apostado)

        if valor_apostado in ['rojo', 'negro']:
            self.__forma_apuesta_elegida = self.__apostar_color(valor_apostado)

        if valor_apostado in ['par', 'impar']:
            self.__forma_apuesta_elegida = self.__apostar_paridad(valor_apostado)


    def apostar(self, cantidad_apostada:int):
        if cantidad_apostada > self.__apuesta_maxima:
            raise ValueError("La cantidad apostada supero el maximo")
        numero_ruleta: int = randint(0, 36)
        self.numeros_salidos[numero_ruleta] += 1
        self.contador_tiradas += 1
        avg = self.promedio_numeros()
        self.historico_promedios.append(avg)


        multiplicador_ganancia: int = self.__forma_apuesta_elegida(numero_ruleta)

        resultado:int
        if multiplicador_ganancia == 0:
            resultado = -cantidad_apostada
        else:
            resultado = cantidad_apostada*multiplicador_ganancia
        return resultado


    def promedio_numeros(self):
        """Calcula el numero promedio salido hasta el momento
        Para esto, se usa la formula de avg = sumatoria(valor*freq_abs_valor)/cantidad_tiradas"""
        sumatoria_freq = 0
        for num,freq in enumerate(self.numeros_salidos):
            sumatoria_freq += num*freq
        avg = sumatoria_freq/self.contador_tiradas
        return avg

    def __apostar_numero(self, numero_elegido: int) -> Callable:
        """Funcion que dado un numero elegido, retorna un entero indicando
        el numero de veces que se gana la cantidad apostada"""

        def apostar(numero_ruleta:int) -> int:
             return 36 if numero_elegido == numero_ruleta else 0

        return apostar

    def __apostar_color(self, color_elegido: str) -> Callable:
        """Funcion que dado un color, retorna un entero indicando
        el numero de veces que se gana la cantidad apostada"""

        def apostar(numero_ruleta:int) -> int:
            if (color_elegido == "rojo" and numero_ruleta in self.numeros_rojos) or (
                    color_elegido == "negro" and numero_ruleta in self.numeros_negros):
                return 2
            else:

                return 0

        return apostar

    def __apostar_paridad(self, paridad_elegida: str) -> Callable:
        """Funcion que dada una paridad elegida (NO SE TOMA EL 0 COMO PAR), retorna un entero indicando
        el numero de veces que se gana la cantidad apostada"""

        def apostar(numero_ruleta:int) -> int:
            def es_par(num: int):
                return num % 2 == 0
            if (paridad_elegida == "impar" and not es_par(numero_ruleta)) or (
                    paridad_elegida == "par" and es_par(numero_ruleta) and numero_ruleta != 0):
                return 2
            else:
                return 0

        return apostar
