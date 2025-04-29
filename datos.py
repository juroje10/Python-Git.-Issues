import json

def cargar_datos(ruta):
    archivo = open(ruta)
    datos = json.load(archivo)
    archivo.close()
    return datos

def guardar_datos(ruta, datos):
    with open(ruta, "w") as archivo:
        archivo.write(json.dumps(datos))
    archivo.close()
    return