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



promedios_historico=[]
freq_rel_historico=[]
varianzas_historico= []
desvios_historico =[]

for j in range(CORRIDAS):
  #Historico de variables para una corrida
  promedio_corrida = []
  freq_rel_corrida = []
  varianza_corrida=[]
  desvio_corrida=[]
  valores = []
  for i in range(CANTIDAD_TIRADAS):
    valor_actual = random.randint(0,36)
    valores.append(valor_actual)

    freq_abs_actual = valores.count(NUMERO_ELEGIDO)
    freq_rel_actual= freq_abs_actual/(i+1)
    freq_rel_corrida.append(freq_rel_actual)

    promedio=np.mean(valores)
    promedio_corrida.append(promedio)

    varianza= np.var(valores)
    varianza_corrida.append(varianza)

    desvio= np.std(valores)
    desvio_corrida.append(desvio)

  print(f"Corrida número: {j}")
  promedios_historico.append(promedio_corrida)
  freq_rel_historico.append(freq_rel_corrida)
  varianzas_historico.append(varianza_corrida)
  desvios_historico.append(desvio_corrida)


plt.subplot(2, 2, 1)
for i, freq_rel_corrida in enumerate(freq_rel_historico):
  plt.plot(freq_rel_corrida, label=i)
plt.title("freq rel historico")
plt.xlabel("n(nro tiradas)")
plt.ylabel("fr(frecuencia relativa)")
plt.axhline(y=FREQ_REL_ESPERADA, color='r', linestyle='-.')


plt.subplot(2, 2, 2)
for i, promedio_corrida in enumerate(promedios_historico):
  plt.plot(promedio_corrida, label=i)
plt.title("Promedio historico")
plt.xlabel("n(nro tiradas)")
plt.ylabel("vp(valor promedio de las tiradas)")
plt.axhline(y=PROMEDIO_ESPERADO, color='r', linestyle='-.')
plt.ylim(0,36)

plt.subplot(2, 2, 3)
for i, desvio_corrida in enumerate(desvios_historico):
  plt.plot(desvio_corrida, label=i)
plt.title("desvio historico")
plt.xlabel("n(nro tiradas)")
plt.ylabel("vd(valor del desvio)")
plt.axhline(y=DESVIO_ESPERADO, color='r', linestyle='-.')

plt.subplot(2, 2, 4)
for i, varianza_corrida in enumerate(varianzas_historico):
  plt.plot(varianza_corrida, label=i)
plt.title("varianza historico")
plt.xlabel("n(nro tiradas)")
plt.ylabel("vv(valor de la varianza)")
plt.axhline(y=VARIANZA_ESPERADA, color='r', linestyle='-.')
plt.tight_layout()
plt.show()