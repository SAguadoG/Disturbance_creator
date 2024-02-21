import os
import numpy as np

# Obtener el directorio actual del script
directorio_actual = os.path.abspath(os.path.dirname(__file__))
print(directorio_actual)

# Crear los directorios una vez antes de iniciar el bucle

os.makedirs(os.path.join(directorio_actual, 'test'), exist_ok=True)
os.makedirs(os.path.join(directorio_actual, 'train'), exist_ok=True)
os.makedirs(os.path.join(directorio_actual, 'val'), exist_ok=True)

def transient_generator():
    for i in range(3601):
        nombre_archivo = f"or_s_{i}.npy"
        ruta_archivo = os.path.join(directorio_actual, 'original_signals', nombre_archivo)

        if os.path.exists(ruta_archivo):
            print(f"Se encontró el archivo {nombre_archivo}")
            # Cargar los datos desde el archivo .npy
            data = np.load(ruta_archivo)
            # Normalizar la señal al rango [-1, 1]
            signal_original = data / np.max(np.abs(data))

            # Parámetros del transitorio
            longitud_signal = len(signal_original)
            duracion_transitorio = np.random.randint(100, 1000)  # Duración del transitorio de 0.01 a 0.1 segundos
            amplitud_transitorio = np.clip(np.random.uniform(0.8, 1.3), 0.8, 1.3)  # Amplitud del transitorio

            # Generar la posición aleatoria para el transitorio
            inicio_transitorio = np.random.randint(0, longitud_signal - duracion_transitorio)

            # Crear la señal del transitorio como un pulso
            signal_transient = np.copy(signal_original)
            signal_transient[inicio_transitorio:(inicio_transitorio + duracion_transitorio)] += amplitud_transitorio

            if i < 2521:
                directorio_destino = os.path.join(directorio_actual, 'train')
            elif i < 3061:
                directorio_destino = os.path.join(directorio_actual, 'test')
            elif i < 3601:
                directorio_destino = os.path.join(directorio_actual, 'val')
            else:
                print(f"No se encontró el archivo {nombre_archivo}")

            nombre_archivo_nuevo = f"transient_s_{i}.npy"
            ruta_archivo_nuevo = os.path.join(directorio_destino, nombre_archivo_nuevo)
            np.save(ruta_archivo_nuevo, signal_transient)
            print(f"Señal con transitorio guardada en {nombre_archivo_nuevo}")

        else:
            print("archivo no encontrado")


transient_generator()

