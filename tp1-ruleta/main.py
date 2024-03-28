import random
import numpy as np
import matplotlib.pyplot as plt
from sys import argv



#EL primer argumento es el nombre del propio archivo, por eso lo omitimos
argumentos_terminal = argv[1:]

if len(argumentos_terminal) != 3:
  print("""Se deben ingresar 3 parametros de terminal.el comando debe tener la siguiente forma
python3 tp1-ruleta/main.py  XXX  YYY  ZZZ).
Donde
  - XXX -> Cantidad de tiradas a la ruleta por corrida
  - YYY -> Cantidad de corridas
  - ZZ -> NUmero elegido""")
  exit()


#Chequeamos que todos los argumentos ingresados sean numericos
if not all([arg.isnumeric() for arg in argumentos_terminal]):
  print("Solo se pueden ingresar argumentos numericos")
  exit()
#CTES DE VALORES ESPERADS
FREQ_REL_ESPERADA=1/37
PROMEDIO_ESPERADO = np.mean(range(37))
VARIANZA_ESPERADA = np.var(range(37))
DESVIO_ESPERADO = np.std(range(37))

#CTES INGRASADAS POR TERMINAL
CANTIDAD_TIRADAS = int(argumentos_terminal[0])
CORRIDAS = int(argumentos_terminal[1])
NUMERO_ELEGIDO= int(argumentos_terminal[2])

#Chequeamos que las cantidades no sean negativas
if CANTIDAD_TIRADAS <0 or CORRIDAS<0:
  print("Tanto la cantidad de tiradas como las corridas deben ser positivas o 0")

#Chequeamos que el numero elegido lo supere los valores posibles
if NUMERO_ELEGIDO>36:
  print("El numero elegido debe estar entre 0 y 36")
  exit()





print(f"""cantidad_tiradas = {CANTIDAD_TIRADAS}
corridas={CORRIDAS}
numero_elegido={NUMERO_ELEGIDO}\n""")





for j in range(CORRIDAS):
  promedio_historico = []
  freq_rel_historico = []
  varianza_historico=[]
  desvio_historico=[]
  valores = []
  for i in range(CANTIDAD_TIRADAS):
    valor_actual = random.randint(0,36)
    valores.append(valor_actual)

    freq_abs_actual = valores.count(NUMERO_ELEGIDO)
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
  plt.axhline(y=DESVIO_ESPERADO, color='r', linestyle='-.')

  plt.subplot(2, 2, 4)
  plt.plot(varianza_historico,label="varianza historico")
  plt.title("varianza historico")
  plt.xlabel("n(nro tiradas)")
  plt.ylabel("vv(valor de la varianza)")
  plt.axhline(y=VARIANZA_ESPERADA, color='r', linestyle='-.')
  plt.tight_layout()
  plt.show()