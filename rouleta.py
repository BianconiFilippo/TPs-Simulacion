import random
import matplotlib.pyplot as plt

# constantes
FREQ_REL_ESPERADA=1/37
PROMEDIO_ESPERADO = 37/2

# variables
cantidad_tiradas = 100 #Cantidad de tiradas por flujo de ejecucion
corridas = 1 #Cantidad de veces que se corren las tiradas
numero_elegido = 0


for _ in range(corridas):
    promedio_historico=[]
    freq_rel_historico=[]
    valores = []
    for i in range(cantidad_tiradas):
       valor_actual = random.randint(0,36)
       valores.append(valor_actual)
       freq_abs_actual = valores.count(numero_elegido)
       freq_rel_actual = frecuencia_relativa/cantidad_tiradas
       freq_rel_historico.append(freq_rel_actual)
       promedio=sum(valores)/i+1
       promedio_historico.append(promedio)
    frecuencia_absoluta = valores.count(numero_elegido)
    frecuencia_relativa =  frecuencia_absoluta/cantidad_tiradas
    freq_rel_historico.append(frecuencia_relativa)
    promedio = sum(valores)/cantidad_tiradas
    promedio_historico.append(promedio)
    plt.plot(promedio_historico,label="promedio historico")
    plt.title("Promedio historico")
    plt.xlabel("n(nro tiradas)")
    plt.ylabel("vp(valor promedio de las tiradas)")
    plt.axhline(y=PROMEDIO_ESPERADO, color='r', linestyle='-.')
    plt.ylim(0,36)
    plt.show()



