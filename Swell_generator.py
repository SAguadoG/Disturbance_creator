import os
import numpy as np
import matplotlib.pyplot as plt

# Obtenemos el directorio actual para trabajar desde aquí.
directorio_actual = os.path.abspath(os.path.dirname(__file__))


def swell_generator():
    # Flag
    se_encontro_archivo = False

    nombre_archivo = "or_s_1.npy"
    # Obtener la ruta completa al archivo
    ruta_archivo = os.path.join(directorio_actual, 'original_signal', nombre_archivo)

    # Procesar el archivo y actualizar el flag si se encuentra
    if os.path.exists(ruta_archivo):
        se_encontro_archivo = True

    if not se_encontro_archivo:
        print("No se encuentra el archivo")
    else:
        print("Se encuentra el archivo")

        # Cargar los datos desde el archivo .npy
        data = np.load(ruta_archivo, allow_pickle=True)

        # Normalizar la señal al rango [-1, 1]
        signal_original = data / np.max(np.abs(data))

        # Parámetros de la amplificación aleatoria
        longitud_signal = len(signal_original)
        duracion_amplificacion = 3000  # en muestras (0.3 segundos a una tasa de muestreo de 10,000 Hz)
        factor_amplitud_min = 1.2
        factor_amplitud_max = 1.7

        # Generar la posición aleatoria para la amplificación
        inicio_amplificacion = np.random.randint(1, longitud_signal - duracion_amplificacion)

        # Generar el factor de amplificación aleatorio
        factor_amplitud = np.random.uniform(factor_amplitud_min, factor_amplitud_max)

        # Aplicar la amplificación en la parte aleatoria de la señal original
        signal_amplificada = np.copy(signal_original)
        signal_amplificada[inicio_amplificacion:(inicio_amplificacion + duracion_amplificacion)] *= factor_amplitud

        # Visualizar la señal original y la señal amplificada
        plt.figure(figsize=(10, 6))

        plt.subplot(2, 1, 1)
        plt.plot(signal_original)
        plt.title('Señal Original')
        plt.xlabel('Muestras')
        plt.ylabel('Amplitud')

        plt.subplot(2, 1, 2)
        plt.plot(signal_amplificada)
        plt.title('Señal Amplificada Aleatoriamente')
        plt.xlabel('Muestras')
        plt.ylabel('Amplitud')

        plt.tight_layout()
        plt.show()


swell_generator()
