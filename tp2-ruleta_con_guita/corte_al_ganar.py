from ruleta import Ruleta
from estrategia import Estrategia
import matplotlib.pyplot as plt

cantidad_ganadas = 16

cantidad_perdidas = 8
caja_inicial = 0
apuesta_maxima = 0
valor_apostado='par'
apuesta_inicial = 10
estrategia_apuesta = 'dalambert'
unidad_dalambert = 2

cantidad_tiradas = cantidad_perdidas+ cantidad_ganadas

historico_caja = [0]
apuesta_maxima = 80

estrategia = Estrategia(apuesta_inicial=apuesta_inicial,
                            estrategia=estrategia_apuesta,
                            unidad_dalambert=unidad_dalambert)

caja_actual = caja_inicial
apuesta_actual = apuesta_inicial
historico_apuestas = [apuesta_actual]
for i in range(cantidad_perdidas):
    caja_actual -= apuesta_actual
    apuesta_actual = estrategia.get_proxima_apuesta(False, apuesta_actual)
    if apuesta_maxima and apuesta_actual> apuesta_maxima:
        apuesta_actual = apuesta_maxima
    historico_caja.append(caja_actual)
    historico_apuestas.append(apuesta_actual)

for i in range(cantidad_ganadas):
    caja_actual += apuesta_actual
    apuesta_actual = estrategia.get_proxima_apuesta(True, apuesta_actual)
    if apuesta_maxima and apuesta_actual> apuesta_maxima:
        apuesta_actual = apuesta_maxima
    historico_caja.append(caja_actual)
    historico_apuestas.append(apuesta_actual)

print(historico_caja)
plt.bar(x=list(range(cantidad_tiradas+1)), height=historico_caja)

plt.axhline(caja_inicial,label = "Caja inicial", color="r")
plt.axhline(historico_caja[len(historico_caja)-1],label = "Apuesta inicial", color="g")
plt.title("Flujo de caja ")
plt.show()

print(historico_apuestas)
plt.bar(x=list(range(cantidad_tiradas+1)), height=historico_apuestas)

plt.axhline(apuesta_inicial,label = "Apuesta inicial", color="g")
plt.axhline(apuesta_maxima,label = "Apuesta maxima", color="r")
plt.title("Historico de apuestas")
plt.show()
