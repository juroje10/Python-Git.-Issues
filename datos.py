import json

def cargar_datos(ruta):
    """
    Carga datos desde un archivo JSON dado su ruta.

    Parámetros:
    ruta (str): Ruta al archivo JSON.

    Retorna:
    dict: Datos cargados desde el archivo.
    """
    archivo = open(ruta)
    datos = json.load(archivo)
    archivo.close()
    return datos

def guardar_datos(ruta, datos):
    with open(ruta, "w") as archivo:
        archivo.write(json.dumps(datos))
    archivo.close()
    return