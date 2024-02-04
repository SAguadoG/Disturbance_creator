import os
import numpy as np

# Obtener el directorio actual del script
directorio_actual = os.path.abspath(os.path.dirname(__file__))


def flicker_generator():
    for i in range(3601):
        nombre_archivo = f"or_s_{i}.npy"
        ruta_archivo = os.path.join(directorio_actual, 'original_signal', nombre_archivo)

        if os.path.exists(ruta_archivo):
            print(f"Se encontró el archivo {nombre_archivo}")
            # Cargar los datos desde el archivo .npy
            data = np.load(ruta_archivo)
            # Normalizar la señal al rango [-1, 1]
            signal_original = data / np.max(np.abs(data))

            # Parámetros del flicker
            longitud_signal = len(signal_original)
            duracion_flicker = 300  # en muestras (0.3 segundos a una tasa de muestreo de 10,000 Hz)
            amplitud_media = 1.0
            desviacion_estandar = 0.1

            # Generar la posición aleatoria para el flicker
            inicio_flicker = np.random.randint(0, longitud_signal - duracion_flicker)

            # Generar el flicker como una serie de muestras que fluctúan alrededor de la amplitud media
            flicker = np.random.normal(amplitud_media, desviacion_estandar, duracion_flicker)

            # Aplicar el flicker en la parte aleatoria de la señal original
            signal_flicker = np.copy(signal_original)
            signal_flicker[inicio_flicker:(inicio_flicker + duracion_flicker)] *= flicker

            # Guardar la señal con flicker en un nuevo archivo
            directorio_destino = os.path.join(directorio_actual, 'flicker_signals')
            os.makedirs(directorio_destino, exist_ok=True)
            nombre_archivo_nuevo = f"flck_s_{i}.npy"
            ruta_archivo_nuevo = os.path.join(directorio_destino, nombre_archivo_nuevo)
            np.save(ruta_archivo_nuevo, signal_flicker)
            print(f"Señal con flicker guardada en {nombre_archivo_nuevo}")
        else:
            print(f"No se encontró el archivo {nombre_archivo}")


flicker_generator()
