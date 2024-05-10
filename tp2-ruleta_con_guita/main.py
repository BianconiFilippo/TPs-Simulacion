from typing import List, Tuple

import numpy as np
import math
from estrategia import Estrategia
from ruleta import Ruleta
import matplotlib.pyplot as plt




#Variables del sistema

#TIPO_CAPITAL: Puede ser 'finito' o 'inifinito'
tipo_capital:str = 'infinito'


apuesta_inicial:int = 10

#caja_inicial: Si el capital es infinito, no se le da pelota
caja_inicial:int = 200
cantidad_corridas:int = 50
cantidad_tiradas:int = 200
apuesta_maxima:int = 50*apuesta_inicial

#Darle bola solo si usas dalambert
unidad_dalambert:int = 2






#Aca setean la estrategia.
#Le tienen que mandar la ruleta que crearon en la linea anterior y
#la estrategia('dalambert', 'fibonacci',...), la unidad dalambert y la apuesta inicial
historicos_caja:List[List[int]] = []
historicos_promedio:List[List[float]]=[]
historicos_apuesta:List[List[float]]=[]
for i in range(cantidad_corridas):

    #Reseteamos las variables
    # Aca se puede poner un valor del 0 al 36 o bien 'par', 'impar', 'rojo' o 'negro'
    ruleta: Ruleta = Ruleta(apuesta_maxima=apuesta_maxima,
                            valor_apostado='par')
    estrategia = Estrategia(apuesta_inicial=apuesta_inicial,
                            estrategia='martingala',
                            unidad_dalambert=unidad_dalambert)
    apuesta_actual: int = apuesta_inicial
    acumulador_apuestas = apuesta_actual
    caja_actual: int = caja_inicial
    historico_caja: List[int] = [caja_actual]
    acumulador_ganacias: int = 0
    ganancia: int = 0
    historico_apuesta:List[int] = [apuesta_actual]
    historico_promedios_numeros : List[float] = []

    for j in range(cantidad_tiradas):
        print(f"TIRADA {j + 1}")
        print(f"{apuesta_actual=} -- {caja_actual=}")
        if (tipo_capital == "finito" and caja_actual - apuesta_actual < 0):
            break
        ganancia:int = 0

        #Revisar apuesta maxima
        if apuesta_actual > apuesta_maxima and apuesta_maxima!= 0:
            apuesta_actual =  apuesta_maxima

        ganancia = ruleta.apostar(apuesta_actual)


        gano_apuesta:bool = ganancia > 0



        #Nota: ganancia puede ser negativo
        caja_actual += ganancia
        acumulador_apuestas += apuesta_actual
        acumulador_ganacias += ganancia

        historico_caja.append(caja_actual)
        historico_apuesta.append(apuesta_actual)

        apuesta_actual = estrategia.get_proxima_apuesta(gano_apuesta, apuesta_actual)


    historicos_caja.append(historico_caja)
    historicos_apuesta.append(historico_apuesta)
    historicos_promedio.append(ruleta.historico_promedios)

for caja in historicos_caja:
    plt.plot(caja)
plt.axhline(caja_inicial,label = "Caja inicial")
plt.title("Flujo de caja ")
plt.show()


for apuestas in historicos_apuesta:
    plt.plot(apuestas)
plt.axhline(apuesta_maxima,label = "Apuesta maxima")
plt.title("Historicos de apuesta")
plt.show()

for avgs in historicos_promedio:
    plt.plot(avgs)
plt.axhline(np.mean(list(range(37))),label = "Valor medio ")
plt.title("Historico del valor medio")
plt.ylim(0,37)
plt.show()



    




