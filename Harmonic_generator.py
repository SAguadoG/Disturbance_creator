import os
import numpy as np

# Obtener el directorio actual del script
directorio_actual = os.path.abspath(os.path.dirname(__file__))


def harmonic_generator():
    for i in range(3601):
        nombre_archivo = f"or_s_{i}.npy"
        ruta_archivo = os.path.join(directorio_actual, 'original_signal', nombre_archivo)

        if os.path.exists(ruta_archivo):
            print(f"Se encontró el archivo {nombre_archivo}")
            # Cargar los datos desde el archivo .npy
            data = np.load(ruta_archivo)
            # Normalizar la señal al rango [-1, 1]
            signal_original = data / np.max(np.abs(data))

            # Parámetros del armónico
            tiempo = np.arange(len(signal_original)) / 10000  # Generar un vector de tiempo (tasa de muestreo de 10,000 Hz)
            num_harmonics = np.random.randint(1, 6)  # Generar un número aleatorio de armónicos (de 1 a 5)
            harmonic_amplitude = 0.1  # Amplitud del armónico

            # Generar la señal armónica sumando múltiples armónicos a la señal original
            harmonic_signal = np.zeros_like(signal_original)
            for _ in range(num_harmonics):
                harmonic_freq = np.random.randint(1, 11) * 50  # Generar un armónico aleatorio entre 50 Hz y 500 Hz
                harmonic_signal += harmonic_amplitude * np.sin(2 * np.pi * harmonic_freq * tiempo)

            # Sumar la señal armónica a la señal original
            signal_with_harmonic = signal_original + harmonic_signal

            # Guardar la señal con armónico en un nuevo archivo
            directorio_destino = os.path.join(directorio_actual, 'harmonic_signals')
            os.makedirs(directorio_destino, exist_ok=True)
            nombre_archivo_nuevo = f"hrc_s_{i}.npy"
            ruta_archivo_nuevo = os.path.join(directorio_destino, nombre_archivo_nuevo)
            np.save(ruta_archivo_nuevo, signal_with_harmonic)
            print(f"Señal con armónico guardada en {nombre_archivo_nuevo}")
        else:
            print(f"No se encontró el archivo {nombre_archivo}")


harmonic_generator()
