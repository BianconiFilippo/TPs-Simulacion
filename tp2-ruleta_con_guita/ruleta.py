from dataclasses import dataclass
from random import randint
from typing import Set, Callable, Union


@dataclass
class Ruleta:
    numeros_rojos: Set[int]
    numeros_negros: Set[int]
    apostar: Callable

    def __init__(self, valor_apostado: str | int):

        self.numeros_rojos = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
        self.numeros_negros = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
        self.set_apuesta(valor_apostado)
        print(f"RULETA: Estas apostando al '{valor_apostado}'")

    def set_apuesta(self, valor_apostado: str| int):
        if not (isinstance(valor_apostado, int) or isinstance(valor_apostado, str)):
            raise TypeError("La apuesta debe ser un entero o una string")
        if not (valor_apostado in [i for i in range(0, 37)] or valor_apostado in ['rojo', 'negro', 'par', 'impar']):
            raise ValueError(
                "No ingreso una apuesta valida, debe ser un valor entre 0 y 36 o bien rojo, negro, par o impar")
        if valor_apostado in [i for i in range(0, 37)]:
            self.apostar = self.__apostar_numero(valor_apostado)

        if valor_apostado in ['rojo', 'negro']:
            self.apostar = self.__apostar_color(valor_apostado)

        if valor_apostado in ['par', 'impar']:
            self.apostar = self.__apostar_paridad(valor_apostado)

    def __apostar_numero(self, numero_elegido: int) -> Callable:
        """Funcion que dado un numero elegido, retorna un entero indicando
        el numero de veces que se gana la cantidad apostada"""

        def apostar() -> int:
            if not isinstance(numero_elegido, int):
                raise TypeError("Debe ingresar un numero")
            if numero_elegido < 0 or numero_elegido > 36:
                raise ValueError("Se ingresó un valor por fuera de los valores permitidos")

            numero_ruleta: int = randint(0, 36)
            return 36 if numero_ruleta == numero_elegido else 0

        return apostar

    def __apostar_color(self, color_elegido: str) -> Callable:
        """Funcion que dado un color, retorna un entero indicando
        el numero de veces que se gana la cantidad apostada"""

        def apostar() -> int:
            numero_ruleta: int = randint(0, 36)
            if (color_elegido == "rojo" and numero_ruleta in self.numeros_rojos) or (
                    color_elegido == "negro" and numero_ruleta in self.numeros_negros):
                return 2
            else:
                return 0

        return apostar

    def __apostar_paridad(self, paridad_elegida: str) -> Callable:
        """Funcion que dada una paridad elegida (NO SE TOMA EL 0 COMO PAR), retorna un entero indicando
        el numero de veces que se gana la cantidad apostada"""

        def apostar() -> int:
            def es_par(num: int):
                return num % 2 == 0

            numero_ruleta: int = randint(0, 36)

            if (paridad_elegida == "impar" and not es_par(numero_ruleta)) or (
                    paridad_elegida == "par" and es_par(numero_ruleta) and numero_ruleta != 0):
                return 2
            else:
                return 0

        return apostar
