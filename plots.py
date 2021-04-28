import matplotlib.pyplot as plt
from pylab import plot, show, title, xlabel, ylabel, subplot
import numpy as np

# Importa fft y arange

from scipy import fft


def plotSeñalModuladora(x, y):
    plt.plot(x, y)
    # Give a title for the sine wave plot

    plt.title('Grafica De Onda Moduladora')

    # Give x axis label for the sine wave plot

    plt.xlabel('Tiempo')

    # Give y axis label for the sine wave plot

    plt.ylabel('Amplitud')
    plt.grid(True, which='both')

    plt.axhline(y=0, color='b')
    plt.show()


def plotSeñalPortadora(x, y):
    plt.plot(x, y)
    # Give a title for the sine wave plot

    plt.title('Grafica De Onda Portadora')

    # Give x axis label for the sine wave plot

    plt.xlabel('Tiempo')

    # Give y axis label for the sine wave plot

    plt.ylabel('Amplitud')
    plt.grid(True, which='both')

    plt.axhline(y=0, color='b')
    plt.show()


def plotSeñalModulada(x, y):
    plt.plot(x, y)
    # Give a title for the sine wave plot

    plt.title('Señal Modulada')

    # Give x axis label for the sine wave plot

    plt.xlabel('Tiempo')

    # Give y axis label for the sine wave plot

    plt.ylabel('Amplitud')
    plt.grid(True, which='both')

    plt.axhline(y=0, color='b')
    plt.show()


def plotSpectrum(y, Fs, t):
    """

    grafica la amplitud del espectro de y(t)

    """

    n = len(y)  # longitud de la señal

    k = np.arange(n)

    T = n / Fs

    frq = k / T  # 2 lados del rango de frecuancia

    frq = frq[range(float(n) / 2)]  # Un lado del rango de frecuencia

    Y = fft(y) / n  # fft calcula la normalizacion

    Y = Y[range(n / 2)]

    plt(frq, abs(Y), 'r')  # grafica el espectro de frecuencia

    xlabel('Frecuencia (Hz)')

    ylabel('|Y(f)|')

    subplot(2, 1, 1)

    plt.plot(t, y)

    xlabel('Tiempo')

    ylabel('Amplitud')

    subplot(2, 1, 2)

    # Se llama a la funcion con la señal y la rata de muestreo

    plt.show()
