import os
import numpy as np
import matplotlib.pyplot as plt


def plot_signal(signal, fs):
    # Plotear la señal en el dominio del tiempo y la frecuencia.
    n = len(signal)
    t = np.arange(0, n) / fs

    # Calcular la transformada de Fourier de la señal
    fft_signal = np.fft.fft(signal)
    freqs = np.fft.fftfreq(n, 1/fs)

    # Plotear la señal y su transformada de Fourier
    fig, ax = plt.subplots(2, 1, figsize=(8, 8))

    ax[0].plot(t, signal)
    ax[0].set_title('Señal original')

    ax[1].plot(freqs[:n//2], np.abs(fft_signal[:n//2]))
    ax[1].set_xlim(0, fs / 10)
    ax[1].set_title('Transformada de Fourier de la señal')

    plt.show()


def plotear_archivo(archivo):
    directorio = os.path.join(os.path.dirname(__file__), 'original_signal')

    # Comprobar si el archivo existe
    ruta_archivo = os.path.join(directorio, archivo)
    if not os.path.exists(ruta_archivo):
        print(f"El archivo {archivo} no existe en la carpeta 'original_signal'.")
        return

    # Cargar el vector desde el archivo .npy
    vector = np.load(ruta_archivo)

    # Configurar la frecuencia de muestreo para la señal (ajustar según sea necesario)
    fs = 1000  # Por ejemplo, 1000 Hz

    # Plotear la señal
    plot_signal(vector, fs)


# Llamada a la función principal
if __name__ == "__main__":
    # Archivo que deseas plotear
    archivo_a_plotear = "or_s_2456.npy"  # Cambiar al nombre del archivo deseado

    # Plotear el archivo especificado
    plotear_archivo(archivo_a_plotear)
