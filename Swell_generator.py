import os
import numpy as np

# Obtener el directorio actual del script
directorio_actual = os.path.abspath(os.path.dirname(__file__))

def swell_generator():
    for i in range(3601):
        nombre_archivo = f"or_s_{i}.npy"
        ruta_archivo = os.path.join(directorio_actual, 'original_signal', nombre_archivo)

        if os.path.exists(ruta_archivo):
            print(f"Se encontró el archivo {nombre_archivo}")
            # Cargar los datos desde el archivo .npy
            data = np.load(ruta_archivo)
            # Normalizar la señal al rango [-1, 1]
            signal_original = data / np.max(np.abs(data))

            # Parámetros de la amplificación aleatoria
            longitud_signal = len(signal_original)
            duracion_amplificacion = 3000  # en muestras (0.3 segundos a una tasa de muestreo de 10,000 Hz)
            factor_amplitud_min = 1.2
            factor_amplitud_max = 1.7

            # Generar la posición aleatoria para la amplificación
            inicio_amplificacion = np.random.randint(0, longitud_signal - duracion_amplificacion)

            # Generar el factor de amplificación aleatorio
            factor_amplitud = np.random.uniform(factor_amplitud_min, factor_amplitud_max)

            # Aplicar la amplificación en la parte aleatoria de la señal original
            signal_amplificada = np.copy(signal_original)
            signal_amplificada[inicio_amplificacion:(inicio_amplificacion + duracion_amplificacion)] *= factor_amplitud

            # Guardar la señal amplificada en un nuevo archivo
            directorio_destino = os.path.join(directorio_actual, 'swell_signals')
            os.makedirs(directorio_destino, exist_ok=True)
            nombre_archivo_nuevo = f"sw_s_{i}.npy"
            ruta_archivo_nuevo = os.path.join(directorio_destino, nombre_archivo_nuevo)
            np.save(ruta_archivo_nuevo, signal_amplificada)
            print(f"Señal amplificada guardada en {nombre_archivo_nuevo}")
        else:
            print(f"No se encontró el archivo {nombre_archivo}")

swell_generator()
