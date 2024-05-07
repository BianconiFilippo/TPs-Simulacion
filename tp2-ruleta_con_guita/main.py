from typing import List, Tuple
from estrategia import Estrategia
from ruleta import Ruleta

#Variables del sistema
#(A INGRESAR POR CONSOLA
apuesta_inicial:int = 2
caja_disponible:int = 500
cantidad_corridas:int = 30
cantidad_tiradas:int = 100

#Darle bola solo si usas dalambert
unidad_dalambert:int = 2


apuesta_actual:int  = apuesta_inicial
caja_actual:int = caja_disponible

historico_caja:List[int] = [caja_actual]


#Aca se puede poner un valor del 0 al 36 o bien 'par', 'impar', 'rojo' o 'negro'
ruleta:Ruleta = Ruleta(valor_apostado = 'impar' )

#Aca setean la estrategia.
#Le tienen que mandar la ruleta que crearon en la linea anterior y
#la estrategia('dalambert', 'fibonacci',...), la unidad dalambert y la apuesta inicial
estrategia:Estrategia = Estrategia(apuesta_inicial = apuesta_inicial,
                                   estrategia= "martingala",
                                   ruleta = ruleta,
                                   unidad_dalambert = unidad_dalambert)
i:int = 0
while i < cantidad_tiradas and caja_actual - apuesta_actual >= 0:
    ganancia:int = 0

    (apuesta_actual, ganancia) = estrategia.apostar(apuesta_actual)

    #Nota: ganancia puede ser negativo
    caja_actual += ganancia
    print(f"CORRIDA {i}")
    print(f"{apuesta_actual=} -- {caja_actual=}")
    historico_caja.append(caja_actual)

    i += 1

print(historico_caja)



    




