import os
import numpy as np

# Obtener el directorio actual del script
directorio_actual = os.path.abspath(os.path.dirname(__file__))
print(directorio_actual)

# Crear los directorios una vez antes de iniciar el bucle

os.makedirs(os.path.join(directorio_actual, 'test'), exist_ok=True)
os.makedirs(os.path.join(directorio_actual, 'train'), exist_ok=True)
os.makedirs(os.path.join(directorio_actual, 'val'), exist_ok=True)


def harmonic_swell_generator():
    for i in range(3601):
        nombre_archivo = f"or_s_{i}.npy"
        ruta_archivo = os.path.join(directorio_actual, 'original_signals', nombre_archivo)

        if os.path.exists(ruta_archivo):
            print(f"Se encontró el archivo {nombre_archivo}")
            # Cargar los datos desde el archivo .npy
            data = np.load(ruta_archivo)
            # Normalizar la señal al rango [-1, 1]
            signal_original = data / np.max(np.abs(data))

            # Parámetros del armónico
            # Generar un vector de tiempo (tasa de muestreo de 10,000Hz)
            tiempo = np.arange(len(signal_original)) / 10000
            num_harmonics = np.random.randint(1, 3)  # Generar un número aleatorio de armónicos (de 1 a 2)
            harmonic_amplitude = 0.1  # Amplitud del armónico

            # Generar la señal armónica sumando múltiples armónicos a la señal original
            harmonic_signal = np.zeros_like(signal_original)
            for _ in range(num_harmonics):
                harmonic_freq = np.random.randint(1, 11) * 50  # Generar un armónico aleatorio entre 50 Hz y 500 Hz
                harmonic_signal += harmonic_amplitude * np.sin(2 * np.pi * harmonic_freq * tiempo)

            # Parámetros del Swell
            longitud_signal = len(signal_original)
            duracion_amplificacion = np.random.randint(3000, 5000)  # 0.3 a 0.5 segundos aleatoriamente
            factor_amplitud_min = 1.2
            factor_amplitud_max = 1.7

            # Generar la posición aleatoria para la amplificación
            inicio_amplificacion = np.random.randint(0, longitud_signal - duracion_amplificacion)

            # Generar el factor de amplificación aleatorio
            factor_amplitud = np.random.uniform(factor_amplitud_min, factor_amplitud_max)

            # Aplicar la amplificación en la parte aleatoria de la señal original
            signal_sag = np.copy(signal_original)
            signal_sag[inicio_amplificacion:(inicio_amplificacion + duracion_amplificacion)] *= factor_amplitud

            # Sumar la señal armónica y la señal con swell
            signal_with_harmonic = signal_original + harmonic_signal
            signal_with_harmonic_and_swell = np.copy(signal_with_harmonic)
            signal_with_harmonic_and_swell[inicio_amplificacion:(inicio_amplificacion + duracion_amplificacion)] *= (
                factor_amplitud)

            if i < 2521:
                directorio_destino = os.path.join(directorio_actual, 'train')
            elif i < 3061:
                directorio_destino = os.path.join(directorio_actual, 'test')
            elif i < 3601:
                directorio_destino = os.path.join(directorio_actual, 'val')
            else:
                print(f"No se encontró el archivo {nombre_archivo}")

            nombre_archivo_nuevo = f"hrc_sw_s_{i}.npy"
            ruta_archivo_nuevo = os.path.join(directorio_destino, nombre_archivo_nuevo)
            np.save(ruta_archivo_nuevo, signal_with_harmonic_and_swell)
            print(f"Señal con armónico y Swell guardada en {nombre_archivo_nuevo}")

        else:
            print("archivo no encontrado")


harmonic_swell_generator()
