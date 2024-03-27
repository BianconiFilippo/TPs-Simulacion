import random
import numpy as np
import matplotlib.pyplot as plt
#CTES
FREQ_REL_ESPERADA=1/37
PROMEDIO_ESPERADO = np.mean(range(37))
varianza_esperada = np.var(range(37))
desvio_esperado = np.std(range(37))

#VARIABLES
cantidad_tiradas = 100
corridas = 3
numero_elegido= 3

for j in range(corridas):
  promedio_historico = []
  freq_rel_historico = []
  varianza_historico=[]
  desvio_historico=[]
  valores = []
  for i in range(cantidad_tiradas):
    valor_actual = random.randint(0,36)
    valores.append(valor_actual)

    freq_abs_actual = valores.count(numero_elegido)
    freq_rel_actual= freq_abs_actual/(i+1)
    freq_rel_historico.append(freq_rel_actual)

    promedio=np.mean(valores)
    promedio_historico.append(promedio)

    varianza= np.var(valores)
    varianza_historico.append(varianza)

    desvio= np.std(valores)
    desvio_historico.append(desvio)

  print(f"Corrida número: {j}")
#graficas
  plt.subplot(2, 2, 1)
  plt.plot(freq_rel_historico,label="frecuencia rel historico")
  plt.title("freq rel historico")
  plt.xlabel("n(nro tiradas)")
  plt.ylabel("fr(frecuencia relativa)")
  plt.axhline(y=FREQ_REL_ESPERADA, color='r', linestyle='-.')


  plt.subplot(2, 2, 2)
  plt.plot(promedio_historico,label="promedio historico")
  plt.title("Promedio historico")
  plt.xlabel("n(nro tiradas)")
  plt.ylabel("vp(valor promedio de las tiradas)")
  plt.axhline(y=PROMEDIO_ESPERADO, color='r', linestyle='-.')
  plt.ylim(0,36)

  plt.subplot(2, 2, 3)
  plt.plot(desvio_historico,label="desvio historico")
  plt.title("desvio historico")
  plt.xlabel("n(nro tiradas)")
  plt.ylabel("vd(valor del desvio)")
  plt.axhline(y=desvio_esperado, color='r', linestyle='-.')

  plt.subplot(2, 2, 4)
  plt.plot(varianza_historico,label="varianza historico")
  plt.title("varainza historico")
  plt.xlabel("n(nro tiradas)")
  plt.ylabel("vv(valor de la varianza)")
  plt.axhline(y=varianza_esperada, color='r', linestyle='-.')
  plt.tight_layout()
  plt.show()