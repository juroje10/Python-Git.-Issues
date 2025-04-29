usuarios = []

def agregar_usuario(nombre, edad):
    for u in usuarios:
        if u["nombre"] == nombre:
            return "Ya existe"
    usuarios.append({"nombre": nombre, "edad": edad})
    return "Agregado"

def borrar_usuario(nombre):
    for i in range(len(usuarios)):
        if usuarios[i]["nombre"] == nombre:
            usuarios.pop(i)
            return "Borrado"
    return "No encontrado"

def agregar_usuario_seguro(nombre, edad, contraseña):
    if contraseña == "1234":
        return agregar_usuario(nombre, edad)
    return "Contraseña incorrecta"
