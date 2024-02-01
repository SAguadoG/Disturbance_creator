import os
import numpy as np
import scipy.io


def extraer_vector(ruta_archivo):
    data = scipy.io.loadmat(ruta_archivo)
    signal = data['signal']
    return signal.flatten()


# Me he descargado una hora revisada y he partido desde ahí.
# por lo tanto la iteración es minuto -> segundo -> decimal.
def buscar_archivo(year, mes, dia, hora):
    directorio_actual = os.path.abspath(os.path.dirname(__file__))
    archivos_encontrados = []

    for minuto in range(60):
        for segundo in range(60):
            for fraccion in range(10):
                nombre_archivo = f"{year}_{mes}_{dia}_{hora}_{minuto}_{segundo}.{fraccion}_lab_politecnica_3a.mat"
                ruta_archivo = os.path.join(directorio_actual, 'raw_signals', nombre_archivo)
                if os.path.exists(ruta_archivo):
                    archivos_encontrados.append(ruta_archivo)

    return archivos_encontrados


def guardar_vector(vector, contador):
    directorio_destino = os.path.join(os.path.dirname(__file__), 'original_signal')
    os.makedirs(directorio_destino, exist_ok=True)
    nombre_archivo = f"or_s_{contador}.npy"
    ruta_archivo_nuevo = os.path.join(directorio_destino, nombre_archivo)
    np.save(ruta_archivo_nuevo, vector)
    print(f"Vector extraído y guardado en {nombre_archivo}")


def obtener_fecha():
    # Tal cual del programa principal, 0 cambios.
    year = input("Ingrese el año: ")
    mes = input("Ingrese el mes: ")
    dia = input("Ingrese el día: ")
    hora = input("Ingrese la hora: ")

    # Dar los datos que tengamos seguro.
    archivos = buscar_archivo(year, mes, dia, hora)

    # Creacion del nuevo .npy
    contador = 1
    for ruta_archivo in archivos:
        vector = extraer_vector(ruta_archivo)
        guardar_vector(vector, contador)
        contador += 1

    # Mostrar mensaje si no se encontraron archivos
    if not archivos:
        print(f"No se encontraron archivos para la fecha proporcionada.")

    # flag para mi, por si va mal la iteración.
    print("Se termina de buscar")


# Llamada a la función principal
if __name__ == "__main__":
    obtener_fecha()
