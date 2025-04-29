def contar_palabras(texto):
    """
    Cuenta cuántas veces aparece cada palabra en un texto.

    Parámetros:
    texto (str): Texto de entrada.

    Retorna:
    dict: Diccionario con palabras como claves y sus frecuencias como valores.
    """
    palabras = texto.split(" ")
    conteo = {}
    for p in palabras:
        if p in conteo:
            conteo[p] = conteo[p] + 1
        else:
            conteo[p] = 1
    return conteo

def palabras_mas_largas(texto):
    palabras = texto.split()
    maximo = 0
    for palabra in palabras:
        if len(palabra) > maximo:
            maximo = len(palabra)

    largas = []
    for palabra in palabras:
        if len(palabra) == maximo:
            if palabra not in largas:
                largas.append(palabra)
    return largas

print(contar_palabras("hola hola qué tal tal estás estás estás"))
print(palabras_mas_largas("un dos tres cuatro cinco seis siete"))


