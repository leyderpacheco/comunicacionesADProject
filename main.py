import numpy as np
import math
import matplotlib
from matplotlib import pyplot as plt
from plots import *
import calculos
# Importa  coseno, linspace y pi

from numpy import cos, linspace, pi

# Importa plot, show, title, xlabel, ylabel y subplot para graficar

from pylab import plot, show, title, xlabel, ylabel, subplot

# Importa fft y arange

from numpy.fft import fft

matplotlib.use('Qt5Agg')

# Programa de Modulacion Angular PM Y FM

print("Programa que le ayuda a modular en FM Y PM")


def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


def PM():
    Vm = float(input("Ingrese la amplitud de su señal moduladora PM"))
    fm = float(input("Ingrese la frecuencia de su señal modularoda PM"))

    Vp = float(input("Ingrese la amplitud de su señal portadora PM "))
    fp = float(input("Ingrese la frecuencia de su señal portadora PM"))

    Fs = 150.0
    Ts = 1.0 / Fs

    time = np.arange(0, 1, Ts)

    myfunction2 = np.vectorize(calculos.moduladoraPM)
    myfunction3 = np.vectorize(calculos.portadoraPM)
    myfunction1 = np.vectorize(calculos.moduladaPM)
    # amplitud = calculos.moduladoraPM(Vm,fm,time)

    plotSeñalModuladora(time, myfunction2(Vm, fm, time))
    plotSeñalPortadora(time, myfunction3(Vp, fp, time))

    m = float(input("Ingrese el indice de modulacion"))

    plotSeñalModulada(time, myfunction1(Vp, time, m, fm))

    print("******************VISUALIZACION DATOS IMPORTANTES******************")
    print("la sensitividad de desviación K para su onda es :")
    print(calculos.sensibilidadK2(Vm, m))
    print("la desviacion maxima de frecuencia Δf es :")
    print(calculos.deltaf(m, fm))
    print("el indice de modulacion m es ")
    print(m)
    print("El ancho de banda es: ")

    if m < np.pi / 2:
        b = 2 * fm
        print(str(b))
    else:
        b = 2 * m*Vm
        print(str(b))

    print("El ancho de banda real requerido es: ")

    print(2 * (calculos.npares(m) * fm))

    RL = float(input("Ingrese la la resistencia de carga para calcular la potencia"))
    print("Potencia de la portadora no modulada es: ")
    print(Vm * Vm / 2 * RL)

    # grafica frecuencia onda moduladora
    y = myfunction2(Vm, fm, time)

    # Proceso de graficar la señal

    subplot(2, 1, 1)

    plot(time, y)

    xlabel('Tiempo')

    ylabel('Amplitud')

    title('Onda Moduladora')

    subplot(2, 1, 2)

    # Se llama a la funcion con la señal y la rata de muestreo

    plotSpectrum(y, Fs)

    show()

    # grafica frecuencia onda portadora
    y = myfunction3(Vp, fp, time)

    # Proceso de graficar la señal

    subplot(2, 1, 1)

    plot(time, y)

    xlabel('Tiempo')

    ylabel('Amplitud')

    title('Onda Portadora')

    subplot(2, 1, 2)

    # Se llama a la funcion con la señal y la rata de muestreo

    plotSpectrum(y, Fs)

    show()

    # grafica frecuencia onda modulada
    y = myfunction1(Vp, time, m, fm)

    # Proceso de graficar la señal

    subplot(2, 1, 1)

    plot(time, y)

    xlabel('Tiempo')

    ylabel('Amplitud')

    title('Onda Modulada')

    subplot(2, 1, 2)

    # Se llama a la funcion con la señal y la rata de muestreo

    plotSpectrum(y, Fs)

    show()


def FM():
    Vm = float(input("Ingrese la amplitud de su señal moduladora FM"))
    fm = float(input("Ingrese la frecuencia de su señal modularoda FM"))

    Vp = float(input("Ingrese la amplitud de su señal portadora FM "))
    fp = float(input("Ingrese la frecuencia de su señal portadora FM"))

    Fs = 150.0
    Ts = 1.0 / Fs
    time = np.arange(0, 1, Ts)

    myfunction2 = np.vectorize(calculos.moduladoraFM)
    myfunction3 = np.vectorize(calculos.portadoraFM)
    myfunction1 = np.vectorize(calculos.moduladaFM)

    plotSeñalModuladora(time, myfunction2(Vm, fm, time))
    plotSeñalPortadora(time, myfunction3(Vp, fp, time))

    f = float(input("Ingrese la desviacion max de frecuencia "))

    plotSeñalModulada(time, myfunction1(Vp, fp, time, fm, f))

    print("******************VISUALIZACION DATOS IMPORTANTES******************")
    print("la sensitividad de desviación K para su onda es :")
    print(calculos.sensibilidadK(Vm, f, fm))
    print("la desviacion maxima de frecuencia Δf es :")
    print(f)
    print("el indice de modulacion m es ")
    print(f / fm)
    print("El Porcentaje de modulación es de")
    print(str(((f / fm) * 100)) + "%")
    print("El ancho de banda es: ")

    if f / fm < np.pi / 2:
        b = 2 * fm
        print(str(b))
    else:
        b = 2 * f
        print(str(b))

    print("El ancho de banda real requerido es: ")

    print(2*(calculos.npares(f / fm)*fm))

    RL = float(input("Ingrese la la resistencia de carga para calcular la potencia"))
    print("Potencia de la portadora no modulada es: ")
    print(Vm*Vm/2*RL)

    # Grafica señal moduladora
    y = myfunction2(Vm, fm, time)

    # Proceso de graficar la señal

    subplot(2, 1, 1)

    plot(time, y)

    xlabel('Tiempo')

    ylabel('Amplitud')

    title('Onda Moduladora')

    subplot(2, 1, 2)

    # Se llama a la funcion con la señal y la rata de muestreo

    plotSpectrum(y, Fs)

    show()

    # Grafica señal portadora
    y = myfunction3(Vp, fp, time)

    # Proceso de graficar la señal

    subplot(2, 1, 1)

    plot(time, y)

    xlabel('Tiempo')

    ylabel('Amplitud')

    title('Onda Portadora')

    subplot(2, 1, 2)

    # Se llama a la funcion con la señal y la rata de muestreo

    plotSpectrum(y, Fs)

    show()

    # Grafica señal modulada
    y = myfunction1(Vp, fp, time, fm, f)

    # Proceso de graficar la señal

    subplot(2, 1, 1)

    plot(time, y)

    xlabel('Tiempo')

    ylabel('Amplitud')

    title('Onda Modulada')

    subplot(2, 1, 2)

    # Se llama a la funcion con la señal y la rata de muestreo

    plotSpectrum(y, Fs)

    show()


def plotSpectrum(y, Fs):
    """

    grafica la amplitud del espectro de y(t)

    """

    n = len(y)  # longitud de la señal

    k = np.arange(n)

    T = n / Fs

    frq = k / T  # 2 lados del rango de frecuancia

    frq = frq[range(int((n / 2)))]  # Un lado del rango de frecuencia

    Y = fft(y) / n  # fft calcula la normalizacion

    Y = Y[range(int((n / 2)))]

    plot(frq, abs(Y), 'r')  # grafica el espectro de frecuencia

    xlabel('Frecuencia (Hz)')

    ylabel('|Y(f)|')


salir = False
opcion = 0

while not salir:
    print("******************INICIO*****************")
    print("1. Calculo PM")
    print("2. Calculo FM")
    print("3. Salir")

    print("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        PM()
    elif opcion == 2:
        FM()
    elif opcion == 3:
        salir = True
    else:
        print("Introduce un numero entre 1 y 3")

print("Fin")
