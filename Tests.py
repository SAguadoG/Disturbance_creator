import os
import numpy as np
import matplotlib.pyplot as plt

# Obtenemos el directorio actual para trabajar desde aquí.
directorio_actual = os.path.abspath(os.path.dirname(__file__))


def plot_swell_signal():
    # Nombre del archivo a graficar
    nombre_archivo = "sw_s_8.npy"
    # Obtener la ruta completa al archivo
    ruta_archivo = os.path.join(directorio_actual, 'swell_signals', nombre_archivo)

    # Verificar si el archivo existe
    if os.path.exists(ruta_archivo):
        print("Se encuentra el archivo")
        # Cargar los datos desde el archivo .npy
        data = np.load(ruta_archivo)

        # Visualizar la señal
        plt.figure(figsize=(8, 6))
        plt.plot(data)
        plt.title('Señal Amplificada')
        plt.xlabel('Muestras')
        plt.ylabel('Amplitud')
        plt.show()
    else:
        print("No se encuentra el archivo")


plot_swell_signal()
