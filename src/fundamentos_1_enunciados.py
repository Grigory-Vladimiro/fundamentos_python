# 🧪 Fundamentos Python I – Enunciados

# ------------------------------
# TIPOS DE DATOS
# ------------------------------

# ✨ Ejercicio 1: ¿Qué tipo es?
# Declara las siguientes variables y usa type() para imprimir qué tipo de dato es cada una:
# a = "Hola"
# b = 25
# c = 3.14
# d = True
# e = None

a = "Hola"
b = 25
c = 3.14
d = True
e = None
print(type(a))
print(type(b)) 
print(type(c))
print(type(d))
print(type(e))

# ✨ Ejercicio 2: Conversión rápida
# Convierte la cadena "42" en número, súmale 8 y muestra el resultado.
# Luego convierte el número 100 en texto y muestra la frase:
# "Tu puntuación final es: 100"

number_str = "42"
number_int = int(number_str)
print(number_int + 8)

numeric_string = "100"
converted_integer = int(numeric_string)
print("Tu puntuación final es:", converted_integer)

# ------------------------------
# VARIABLES
# ------------------------------

# ✨ Ejercicio 3: Nombres y saludos
# Crea una variable nombre y una variable edad.
# Imprime una frase como:
# Hola, me llamo X y tengo Y años.

a = "Grigory"
b = 39
print("Hola, soy", a, "y tengo", b, "años.")

# ✨ Ejercicio 4: Intercambio simple
# Tienes dos variables:
# x = "gato"
# y = "perro"
# Intercambia sus valores para que x valga "perro" y y valga "gato".

x = "gato"
y = "perro"

x,y = y, x

print("x", x)
print("y", y)

# ------------------------------
# OPERADORES
# ------------------------------

# ✨ Ejercicio 5: Suma de la compra
# Declara tres precios:
# pan = 1.50
# leche = 1.24
# huevos = 2.70
# Calcula el total y muestra: “El total de tu compra es de: 4,25€”

# ✨ Ejercicio 6: ¿Par o impar?
# Pide al usuario un número con input() y di si es par o impar.

def calcular_total(pan, leche, huevos):
    return pan + leche + huevos

pan = 1.20
leche = 0.95
huevos = 2.10

resultado = f"{calcular_total(pan, leche, huevos):.2f}"
resultado_con_coma = resultado.replace('.', ',')

print("El total de tu compra es de:", resultado_con_coma, "€")

# ------------------------------
# ESTRUCTURAS DE CONTROL
# ------------------------------

# ✨ Ejercicio 7: ¿Mayor de edad?
# Pide la edad al usuario. Si tiene 18 o más, muestra “Puedes entrar”.
# Si no, muestra “Acceso denegado”.

n = int(input("Introduce su edad: "))
if n >= 18:
    print(n,"Puedes entar.")
else:
    print(n,"Acceso denegado.")

# ✨ Ejercicio 8: Elige una opción
# Pide al usuario que elija una opción:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión
# Y muestra un mensaje distinto para cada caso.

def option_1():
    print("Has elegido 1.Ver perfil.")
def option_2():
    print("Has elegido 2.Editar perfil.")
def option_3():
    print("Has elegido 3.Cerrar sesión.")

def main_menu():
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")

while True:
    choice = input("Haga su elección (1-3): ")
    if choice == "1":
        option_1()
    elif choice == "2":
        option_2()
    elif choice == "3":
        option_3()
    elif choice == "0":
        print("Hasta luego!")
        break
    else:
        print("Elección no válida. Por favor, inténtelo de nuevo.")

# ------------------------------
# EXTRA: TIPOS + CONDICIONAL
# ------------------------------

# ✨ Ejercicio 9: Detector de tipos raros
# Pide al usuario que escriba cualquier cosa.
# Muestra:
# - Si es un número entero: “Has escrito un número entero”
# - Si es un número decimal: “Has escrito un número decimal”
# - Si es un texto: “Parece que es una cadena de texto”
# - Si no puedes adivinar el tipo: “No sé qué es esto 😵‍💫”
# Usa try/except para intentar convertir a int() o float().

entrada = input("Escribe algo: ")
try:
    valor = int(entrada)
    print("Has escrito un número entero:")
except ValueError:
    try:
        valor = float(entrada)
        print("Has escrito un número decimal:")
    except ValueError:
        if entrada.isalpha():
            print("Parece que es una cadena de texto")
        else:
            print("No sé qué es esto")

# ------------------------------
# OPERADORES + CONDICIONALES + VARIABLES
# ------------------------------

# ✨ Ejercicio 10: Calculadora con menú
# Pide dos números y muestra este menú:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# Según la opción elegida, haz la operación y muestra el resultado.
# Bonus: si elige dividir y el segundo número es 0, muestra “No se puede dividir por cero”.

num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))

print("Elige una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Escribe el número de la operación que quieres realizar: ")
if opcion == "1":
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
elif opcion == "3":
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)
elif opcion == "4":
    if num2 == 0:
        print("No se puede dividir por cero.")
    else:
        resultado = num1 / num2
        print("El resultado de la divisió es:", resultado)
else:
    print("Operación no válida.")

# ------------------------------
# ESTRUCTURA DE CONTROL CON RANGOS
# ------------------------------

# ✨ Ejercicio 11: Clasificador de edad
# Pide al usuario su edad y clasifícalo:
# - Menor de 3: “Bebé”
# - Entre 3 y 12: “Infancia”
# - Entre 13 y 17: “Adolescencia”
# - Entre 18 y 64: “Adulto”
# - 100 o más: “Senior”

edad = int(input("Cual es tu edad: "))

if edad < 3:
    print("Bebé")
elif 3 <= edad <= 12:
    print("Infancia")
elif 13 <= edad <= 17:
    print("Adolescencia")
elif 18 <= edad <= 64:
    print("Adulto")
elif edad >= 100:
    print("Senior")
else:
    print("Edad no clasificada")