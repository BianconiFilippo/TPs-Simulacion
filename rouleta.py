import random
import matplotlib.pyplot as plt
#CTES
FREQ_REL_ESPERADA=1/37
PROMEDIO_ESPERADO = 37/2


#VARIABLES
cantidad_tiradas = 100
corridas = 3
numero_elegido= 3




for _ in range(corridas):
  promedio_historico = []
  freq_rel_historico = []
  valores = []
  for i in range(cantidad_tiradas):
    valor_actual = random.randint(0,36)
    valores.append(valor_actual)
    freq_abs_actual = valores.count(numero_elegido)
    freq_rel_actual= freq_abs_actual/cantidad_tiradas
    freq_rel_historico.append(freq_rel_actual)
    promedio=sum(valores)/(i+1)
    promedio_historico.append(promedio)
  freq_abs = valores.count(numero_elegido)
  freq_rel= freq_abs/cantidad_tiradas
  freq_rel_historico.append(freq_rel)
  promedio = sum(valores)/cantidad_tiradas
  promedio_historico.append(promedio)
  plt.plot(promedio_historico,label="promedio historico")
  plt.title("Promedio historico")
  plt.xlabel("n(nro tiradas)")
  plt.ylabel("vp(valor promedio de las tiradas)")
  plt.axhline(y=PROMEDIO_ESPERADO, color='r', linestyle='-.')
  plt.ylim(0,36)
  plt.show()