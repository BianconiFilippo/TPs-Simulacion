import matplotlib.pyplot as plt
from os import system
from random import randint

r1 = ""


class num_ruleta:
    def __init__(self, numero, color, fila, columna):
        self.num = numero
        self.color = color
        self.fila = fila
        self.columna = columna

        pass


pass


class ruleta:
    global numeros
    global pago
    global tirada

    def __init__(self):
        num = []

        N0 = num_ruleta(0, "V", 0, 0)
        num.append(N0)
        N1 = num_ruleta(1, "R", 1, 1)
        num.append(N1)
        N2 = num_ruleta(2, "N", 1, 2)
        num.append(N2)
        N3 = num_ruleta(3, "R", 1, 3)
        num.append(N3)
        N4 = num_ruleta(4, "R", 2, 1)
        num.append(N4)
        N5 = num_ruleta(5, "N", 2, 2)
        num.append(N5)
        N6 = num_ruleta(6, "R", 2, 3)
        num.append(N6)
        N7 = num_ruleta(7, "R", 3, 1)
        num.append(N7)
        N8 = num_ruleta(8, "N", 3, 2)
        num.append(N8)
        N9 = num_ruleta(9, "R", 3, 3)
        num.append(N9)
        N10 = num_ruleta(10, "N", 4, 1)
        num.append(N10)
        N11 = num_ruleta(11, "N", 4, 2)
        num.append(N11)
        N12 = num_ruleta(12, "R", 4, 3)
        num.append(N12)
        N13 = num_ruleta(13, "N", 5, 1)
        num.append(N13)
        N14 = num_ruleta(14, "R", 5, 2)
        num.append(N14)
        N15 = num_ruleta(15, "N", 5, 3)
        num.append(N15)
        N16 = num_ruleta(16, "R", 6, 1)
        num.append(N16)
        N17 = num_ruleta(17, "N", 6, 2)
        num.append(N17)
        N18 = num_ruleta(18, "R", 6, 3)
        num.append(N18)
        N19 = num_ruleta(19, "R", 7, 1)
        num.append(N19)
        N20 = num_ruleta(20, "N", 7, 2)
        num.append(N20)
        N21 = num_ruleta(21, "R", 7, 3)
        num.append(N21)
        N22 = num_ruleta(22, "N", 8, 1)
        num.append(N22)
        N23 = num_ruleta(23, "R", 8, 2)
        num.append(N23)
        N24 = num_ruleta(24, "N", 8, 3)
        num.append(N24)
        N25 = num_ruleta(25, "R", 9, 1)
        num.append(N25)
        N26 = num_ruleta(26, "N", 9, 2)
        num.append(N26)
        N27 = num_ruleta(27, "R", 9, 3)
        num.append(N27)
        N28 = num_ruleta(28, "N", 10, 1)
        num.append(N28)
        N29 = num_ruleta(29, "N", 10, 2)
        num.append(N29)
        N30 = num_ruleta(30, "R", 10, 3)
        num.append(N30)
        N31 = num_ruleta(31, "N", 11, 1)
        num.append(N31)
        N32 = num_ruleta(32, "R", 11, 2)
        num.append(N32)
        N33 = num_ruleta(33, "N", 11, 3)
        num.append(N33)
        N34 = num_ruleta(34, "R", 12, 1)
        num.append(N34)
        N35 = num_ruleta(35, "N", 12, 2)
        num.append(N35)
        N36 = num_ruleta(36, "R", 12, 3)
        num.append(N36)

        self.numeros = num

    pass

    def apuesta(self, apostado, apuesta):
        global negro
        global verde
        n = self.untiro()
        ganador = self.numeros[n]
        premio = 0
        if apuesta == str(ganador.num):
            premio = apostado * 36
        elif apuesta == ganador.color:
            premio = apostado * 2
        elif apuesta == str(ganador.fila):
            premio = apostado * 12
        elif apuesta == str(ganador.columna):
            premio = apostado * 3
        if (ganador.color == 'N'):
            negro +=1
        else:
            if(ganador.color== 'V'):
                verde+=1
        return premio

    pass

    def untiro(self):
        self.tirada = randint(0, 36)
        n = self.tirada
        return n


pass

CAPITAL_INICIAL = 1000
MONTO_APUESTA_INICIAL = 100
secuencia = []
negro = 0
verde = 0

def grafica_flujo_caja(fc):
    plt.figure('FLUJO DE CAJA')
    plt.title('Evolución del flujo de caja respecto a n')
    plt.plot(fc, 'r-', label='Flujo de caja')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Cantidad de capital')
    plt.axhline(CAPITAL_INICIAL, label='Flujo de caja inicial')
    plt.legend()
    plt.show()


def grafica_flujo_caja_poblacion(poblacion):
    plt.figure('FLUJO DE CAJA')
    for i in range(0, len(poblacion)):
        plt.plot(poblacion[i])
    plt.title('Evolución del flujo de caja respecto a n para una poblacion')
    #  plt.plot(fc, 'r-', label='Flujo de caja')
    plt.xlabel('Número de tiradas')
    plt.ylabel('Cantidad de capital')
    plt.axhline(CAPITAL_INICIAL, label='Flujo de caja inicial')
    plt.legend()
    plt.grid()
    plt.show()


def grafica_frecuencia(fr):
    plt.figure('FRECUENCIA')
    plt.title('Evolución de la frecuencia relativa de la obtencion la respuesta favorable respecto a n')
    plt.bar(range(len(fr)), fr)
    plt.xlabel('Número de tiradas')
    plt.ylabel('Frecuencia relativa')
    plt.show()


def grafica_torta(rojo, negro, verde ):
    plt.figure('COLOR')
    plt.title('Distribucion del color de los valores obtenidos en la ruleta en n tiros')
    plt.pie(x=[rojo,negro, verde], colors=['red', 'grey','green'], labels=["ROJO", "NEGRO", "VERDE"], autopct='%1.2f%%')
    plt.show()


def martingala():
    rulet = ruleta()
    flujo_caja = []
    frecuencia = []
    global CAPITAL_INICIAL
    global MONTO_APUESTA_INICIAL
    global verde
    global negro
    capital = CAPITAL_INICIAL
    monto_apuesta = MONTO_APUESTA_INICIAL
    color_apostado = "R"
    i = 0
    favorables = 0
    cont_tiradas = 1000  #Contador limite de tiradas para captal infinito

    if (CAPITAL_INFINITO == 'N'):
        while capital >= monto_apuesta:

            capital -= monto_apuesta

            premio = rulet.apuesta(monto_apuesta, color_apostado)
            if (premio != 0):
                capital += premio
                monto_apuesta = MONTO_APUESTA_INICIAL
                favorables += 1
            else:
                monto_apuesta *= 2

            i += 1

            frecuencia.append(favorables / i)
            flujo_caja.append(capital)

        print(frecuencia)
        grafica_flujo_caja(flujo_caja)
        grafica_frecuencia(frecuencia)
        grafica_torta(favorables, negro, verde)
    else:  # PARA CAPITAL INFINITO
        for x in range(0, cont_tiradas):

            premio = rulet.apuesta(monto_apuesta, color_apostado)
            capital -= monto_apuesta
            if (premio != 0):
                capital += premio
                monto_apuesta = MONTO_APUESTA_INICIAL
                favorables += 1
            else:

                monto_apuesta *= 2

            i += 1

            frecuencia.append(favorables / i)
            flujo_caja.append(capital)
        grafica_flujo_caja(flujo_caja)
        grafica_frecuencia(frecuencia)
        grafica_torta(favorables, negro, verde)

def martingala_poblacion():
    rulet = ruleta()
    flujo_caja = []
    frecuencia = []
    poblacion = []
    global CAPITAL_INICIAL
    global MONTO_APUESTA_INICIAL
    capital = CAPITAL_INICIAL
    monto_apuesta = MONTO_APUESTA_INICIAL
    color_apostado = "R"
    i = 0
    favorables = 0
    cont_tiradas = 200 #contador limite de tiradas por corrida para capital infinito
    cont_corridas = 50 #cantidad de corridas para una poblacion
    for i in range(0, cont_corridas):
        if (CAPITAL_INFINITO == 'N'):
            while capital >= monto_apuesta:
                        capital -= monto_apuesta
                        premio = rulet.apuesta(monto_apuesta, color_apostado)
                        if (premio != 0):
                            capital += premio
                            monto_apuesta = MONTO_APUESTA_INICIAL
                            favorables += 1
                        else:
                            monto_apuesta *= 2
                        i += 1
                        frecuencia.append(favorables / i)
                        flujo_caja.append(capital)
        else:  # PARA CAPITAL INFINITO
            for x in range(0, cont_tiradas):
                premio = rulet.apuesta(monto_apuesta, color_apostado)
                capital -= monto_apuesta
                if (premio != 0):
                    capital += premio
                    monto_apuesta = MONTO_APUESTA_INICIAL
                    favorables += 1
                else:
                    monto_apuesta *= 2
                i += 1
                frecuencia.append(favorables / i)
                flujo_caja.append(capital)
        poblacion.append(flujo_caja)
        flujo_caja = []
        frecuencia = []
        capital = CAPITAL_INICIAL
        monto_apuesta = MONTO_APUESTA_INICIAL
        color_apostado = "R"
        i = 0
        favorables = 0
    grafica_flujo_caja_poblacion(poblacion)


def secuencia_fibonacci():
    global secuencia
    first = 0
    second = 1
    sum = 0
    secuencia.append(0)
    for i in range(0, 100):
        first = second
        second = sum
        sum = first + second
        secuencia.append(sum)


def fibonacci():
    rulet = ruleta()
    flujo_caja = []
    frecuencia = []
    global CAPITAL_INICIAL
    global MONTO_APUESTA_INICIAL
    capital = CAPITAL_INICIAL

    color_apostado = "R"
    i = 0
    favorables = 0

    cont_tiradas = 50  # Puede ser mucho mayor. Contador de tiras para capital infinito

    n = 1
    secuencia_fibonacci()
    monto_apuesta = secuencia[n] * 100
    if (CAPITAL_INFINITO == 'N'):
        while capital >= monto_apuesta:
            monto_apuesta = secuencia[n] * 100
            capital -= monto_apuesta
            premio = rulet.apuesta(monto_apuesta, color_apostado)
            if (premio != 0):
                capital += premio
                if n >= 3:
                    n -= 2
                else:
                    n = 1
                favorables += 1
            else:
                n += 1
            i += 1
            frecuencia.append(favorables / i)
            flujo_caja.append(capital)
        grafica_flujo_caja(flujo_caja)
        grafica_frecuencia(frecuencia)
        grafica_torta(favorables, negro, verde)
    else:  # PARA CAPITAL INFINITO
        n = 1
        for x in range(0, cont_tiradas):
            monto_apuesta = secuencia[n] * 10
            capital -= monto_apuesta
            premio = rulet.apuesta(monto_apuesta, color_apostado)
            if (premio != 0):
                capital += premio
                if n >= 2:
                    n -= 2
                else:
                    n = 0

                favorables += 1

            else:
                n += 1

            i += 1
            frecuencia.append(favorables / i)
            flujo_caja.append(capital)

        grafica_flujo_caja(flujo_caja)
        grafica_frecuencia(frecuencia)
        grafica_torta(favorables, negro, verde)


def fibonacci_poblacion():
    flujo_caja = []
    frecuencia = []
    poblacion = []
    rulet = ruleta()
    global CAPITAL_INICIAL
    global MONTO_APUESTA_INICIAL
    capital = CAPITAL_INICIAL
    n = 1
    color_apostado = "R"
    secuencia_fibonacci()
    monto_apuesta = secuencia[n] * 10
    favorables = 0
    cont_tiradas = 1000#contador limite de tiradas por corrida para capital infinito
    cont_corridas = 25 #cantidad de corridas para una poblacion
    for i in range(0,cont_corridas):
        if (CAPITAL_INFINITO == 'N'):
            while capital >= monto_apuesta:
                monto_apuesta = secuencia[n] * 100
                capital -= monto_apuesta
                premio = rulet.apuesta(monto_apuesta, color_apostado)
                if (premio != 0):
                    capital += premio
                    if n >= 3:
                        n -= 2
                    else:
                        n = 1
                    favorables += 1
                else:
                    n += 1
                i += 1
                frecuencia.append(favorables / i)
                flujo_caja.append(capital)
        else:  # PARA CAPITAL INFINITO
            n = 1
            for x in range(0, cont_tiradas):
                monto_apuesta = secuencia[n] * 10
                capital -= monto_apuesta
                premio = rulet.apuesta(monto_apuesta, color_apostado)
                if (premio != 0):
                    capital += premio
                    if n >= 2:
                        n -= 2
                    else:
                        n = 0

                    favorables += 1

                else:
                    n += 1

                i += 1
                flujo_caja.append(capital)
        poblacion.append(flujo_caja)
        flujo_caja = []
        frecuencia = []
        rulet = ruleta()
        capital = CAPITAL_INICIAL
        secuencia_fibonacci()
        n = 1
        monto_apuesta = secuencia[n] * 10
        color_apostado = "R"
        favorables = 0
    grafica_flujo_caja_poblacion(poblacion)


system("cls")
CAPITAL_INFINITO = 'S'
fibonacci()
fibonacci_poblacion()
martingala()
martingala_poblacion()
