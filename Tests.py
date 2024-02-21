import os
import numpy as np
import matplotlib.pyplot as plt

# Obtener el directorio actual para trabajar desde aquí.
directorio_actual = os.path.abspath(os.path.dirname(__file__))


def plot_harmonic_signal():
    # Nombre del archivo a graficar
    nombre_archivo = "hrc_sw_s_3062.npy"
    # Obtener la ruta completa al archivo
    ruta_archivo = os.path.join(directorio_actual, 'val', nombre_archivo)

    # Verificar si el archivo existe
    if os.path.exists(ruta_archivo):
        print("Se encuentra el archivo")
        # Cargar los datos desde el archivo .npy
        data = np.load(ruta_archivo)

        # Visualizar la señal en el dominio del tiempo
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.plot(data)
        plt.title('Señal en el Dominio del Tiempo')
        plt.xlabel('Muestras')
        plt.ylabel('Amplitud')

        # Calcular la transformada de Fourier de la señal
        fft_result = np.fft.fft(data)
        n = len(data)
        freq = np.fft.fftfreq(n, d=1/10000)  # Calcula las frecuencias correspondientes a las componentes de Fourier

        # Limitar el rango de frecuencias para mostrar solo los primeros 10 armónicos (hasta 500 Hz)
        freq_limit = freq[:n//2]
        fft_result_limit = fft_result[:n//2]

        # Visualizar la magnitud de la transformada de Fourier
        plt.subplot(1, 2, 2)
        plt.plot(freq_limit, np.abs(fft_result_limit))
        plt.title('Transformada de Fourier')
        plt.xlabel('Frecuencia (Hz)')
        plt.ylabel('Amplitud')
        plt.xlim(0, 500)  # Limitar el rango de frecuencias en el eje x hasta 500 Hz
        plt.grid(True)
        plt.show()
    else:
        print("No se encuentra el archivo")


plot_harmonic_signal()
