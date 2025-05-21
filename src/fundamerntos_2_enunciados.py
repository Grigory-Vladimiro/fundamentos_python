# 🧪 Fundamentos Python II
# Listas, Tuplas, Diccionarios, Sets

# ------------------------------
# LISTAS
# ------------------------------

# ✨ Ejercicio 1: Lista de la compra
# Crea una lista con al menos 5 elementos. Muestra el primero y el último elemento.

a = ["manzana", "banana", "naranja", "uva", "kiwi"]
print("Primer elemento:", a[0])
print("Ultimo elemento:", a[-1])

# ✨ Ejercicio 2: Añadir y eliminar
# Añade un nuevo elemento a la lista anterior y elimina otro. Imprime la lista actualizada.

a.append("pera")
a.remove("banana")
print(a)

# ✨ Ejercicio 3: Ordenar números
# Crea una lista de números desordenados y ordénala de menor a mayor.

b = [5, 2, 9, 1, 5, 6]
b.sort()
print(b)

# ------------------------------
# TUPLAS
# ------------------------------

# ✨ Ejercicio 4: Coordenadas
# Crea una tupla con una coordenada (latitud, longitud) y muéstrala.

coordenada = (40.4168, -3.7038)  # Ejemplo: Madrid
print(f"Coordenada: latitud {coordenada[0]}, longitud {coordenada[1]}")

# ✨ Ejercicio 5: Elemento fijo
# Crea una tupla de 3 elementos. Intenta cambiar uno y observa qué sucede.

tupla = (1, 2, 3)
tupla_modificada = (4, tupla[1], tupla[2])  # Cambiamos el primer elemento
print(tupla_modificada)

# ------------------------------
# DICCIONARIOS
# ------------------------------

# ✨ Ejercicio 6: Diccionario de usuario
# Crea un diccionario con las claves: nombre, edad, ciudad.

usuario = {
    "nombre": "Grigory",
    "edad": 39,
    "ciudad": "Oviedo"
}
print(usuario)

# ✨ Ejercicio 7: Actualizar valores
# Cambia el valor de ciudad y añade una nueva clave llamada email.

usuario["ciudad"] = "Gijón"
usuario["email"] = "grigori.vladimiro@gmail.com"
print(usuario)

# ✨ Ejercicio 8: Iterar claves y valores
# Imprime cada clave y su valor en una línea distinta.

for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# ------------------------------
# SETS
# ------------------------------

# ✨ Ejercicio 9: Eliminar duplicados
# A partir de una lista con nombres repetidos, crea un set para mostrar solo los nombres únicos.

nombres = ["Nau", "Eva", "Mabel", "Jesus", "Grigory", "Eva", "Nau", "Jesus", "Mabel"]
nombres_unicos = set(nombres)
print(nombres_unicos)

# ✨ Ejercicio 10: Operaciones de conjuntos
# Dado dos sets A y B, muestra qué elementos están en A pero no en B.

A = {"manzana", "pera", "plátano", "kiwi"}
B = {"pera", "kiwi", "melón"}
solo_en_A = A - B
print(solo_en_A)

# ------------------------------
# EXTRA
# ------------------------------

# 🌟 Ejercicio Extra: Mezcla total
# Crea un diccionario donde cada clave sea el nombre de una persona y el valor una lista de hobbies.
# Añade un nuevo hobby a una persona y muestra todos los hobbies de otra.

personas = {
    "Ana": ["tejer", "cine", "cocinar"],
    "Grigory": ["correr", "jugar consola", "fútbol"]
}
personas["Ana"].append("yoga")
print(f"Hobbies de Grigory: {', '.join(personas['Grigory'])}")
print(personas["Ana"])