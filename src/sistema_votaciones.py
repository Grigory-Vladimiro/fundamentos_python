peliculas {}
import csv

def añadir_pelicula():
    nombre = input("Introduce el nombre de la película: ").strip()
    if nombre in peliculas:
        print("La película ya está registrada.")
    else:
        peliculas[nombre] = 0
        print(f"Película '{nombre}' añadida con éxito.")