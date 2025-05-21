# 🌟 Reto: Gestor de contactos

# 🎯 Objetivo:
# Crear una pequeña aplicación en consola que permita al usuario
# almacenar, mostrar y buscar contactos usando listas y diccionarios.

# Instrucciones:

# 1. Añadir un contacto:
#    - Pide al usuario el nombre, edad y ciudad.
#    - Guarda el contacto en una lista como un diccionario.

# 2. Mostrar todos los contactos:
#    - Recorre la lista y muestra los datos en el formato:
#      Nombre: Marta – Edad: 30 – Ciudad: Oviedo

# 3. Buscar por nombre:
#    - Pide un nombre y muestra el contacto si existe.

# 4. Salir:
#    - Si el usuario elige la opción 4, termina el programa.

# 💡 Menú sugerido:
# ¿Qué quieres hacer?
# 1. Añadir contacto
# 2. Ver contactos
# 3. Buscar por nombre
# 4. Salir

agenda = []

def mostrar_menu():
    print("¿Qué quieres hacer?")
    print("1. Añadir contacto")
    print("2. Ver contactos")
    print("3. Buscar por nombre")
    print("4. Salir")

def añadir_contacto():
    nombre = input("Introduce el nombre: ")
    edad = input("Introduce la edad: ")
    ciudad = input("Introduce la ciudad: ")
    
    contacto = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }
    agenda.append(contacto)
    print(f"Contacto añadido correctamente.")

def ver_contactos():
    if not agenda:
        print("No hay contactos guardados.")
        return
    for contacto in agenda:
        print(f"Nombre: {contacto['nombre']} - Edad: {contacto['edad']} - Ciudad: {contacto['ciudad']}")

def buscar_contacto():
    nombre_buscado = input("Introduce el nombre del contacto a buscar: ")
    encontrados = [contacto for contacto in agenda if contacto['nombre'].lower() == nombre_buscado.lower()]
    if encontrados:
        for contacto in encontrados:
            print(f"Nombre: {contacto['nombre']} - Edad: {contacto['edad']} - Ciudad: {contacto['ciudad']}")
    else:
        print("Contacto no encontrado.")
    
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-4): ")
    
    if opcion == "1":
        añadir_contacto()
    elif opcion == "2":
        ver_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        print("Hasta luego.")
        break
    else:
        print("Opción no válida. Por favor, elige otra opción.")