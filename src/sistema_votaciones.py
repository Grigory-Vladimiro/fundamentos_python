peliculas {}
import csv

def añadir_pelicula():
    nombre = input("Introduce el nombre de la película: ").strip()
    if nombre in peliculas:
        print("La película ya está registrada.")
    else:
        peliculas[nombre] = 0
        print(f"Película '{nombre}' añadida con éxito.")

def votar_pelicula():
    nombre = input("Por qué película quieres votar? ").strip()
    try:
        peliculas[nombre] += 1
        print(f"Has votado por '{nombre}'.")
    except KeyError:
        print("Error: La película no está registrada. Intenta otra.")