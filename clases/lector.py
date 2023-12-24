import sys

import clases.juegos
from clases.juegos import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from clases.globales import mi_variable_global

# se abre la ruta del archivo

# Define un diccionario que asocie las variables globales con las funciones respectivas
funciones_juegos = {
    "Vampire": clases.juegos.vampire,
    "MetalSlug": clases.juegos.metalSlug,
    "Mortal": clases.juegos.mortal_kombat,
    "Pesca": clases.juegos.Pesca,
    # Agrega más juegos aquí si es necesario
}


def obtener_path():

    file_path = "C:/Users/R20/Desktop/pi-billion.txt" #filedialog.askopenfilename(title="Selecciona un archivo")

    if not file_path:
        messagebox.showinfo("Error", "No se selecciono un archivo")
        sys.exit("Error")

    return file_path

# Se lee el archivo donde tenemos pi
def leerarchivo(file_path):

    try:
        with open(file_path, 'r') as file:
            archivotxxt = file.read()

            print("Archivo leido exitosamente")
            time.sleep(2)

    except FileNotFoundError:
        print("Archivo no encontrado, Por favor revisar la ruta")
    except Exception as e:
        print(f"Ocurrio un error: {e}")

    return archivotxxt

def recorrer_pi(archivotxxt):

    # tomamos cada numero de pi y lo mandamos a juegos.py donde lo convierte a inputs de taclado solo es necesario cambiar el clase.juegos.xxx por el deseado
    for index in range(len(archivotxxt)):
        if clases.globales.mi_variable_global == "Cerrar":
            break

        numeroPI = archivotxxt[index]
        # verificamos la variable global que mandamos desde interfaz en la clase enviar_nombre y con ello indicaremos cual juego es el que queremos llamar desde la clase juegospy
        funcion_juego = funciones_juegos.get(clases.globales.mi_variable_global)
        print(funcion_juego(numeroPI, index))

# Este se manda llamar para iniciar con la lectura de el archivo.

def iniciarlector():

 file_path = obtener_path()
 if file_path:
   archivotxxt = leerarchivo(file_path)
   if archivotxxt:
    recorrer_pi(archivotxxt)

