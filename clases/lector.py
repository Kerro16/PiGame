import clases.juegos
from clases.juegos import *
import tkinter as tk
from tkinter import filedialog


def obtener_path():
    root = tk.Tk()
    root.withdraw()
    file_path =  "C:/Users/R20/Desktop/pi-billion.txt"           #filedialog.askopenfilename(title="Selecciona un archivo")
    return file_path

def leerarchivo(file_path):
    try:
        with open(file_path, 'r') as file:
            archivotxxt = file.read()

            print("Archivo leido exitosamente")
            time.sleep(2)

            for index in range(len(archivotxxt)):
                numeroPI = archivotxxt[index]
                print(clases.juegos.metalSlug(numeroPI, index))

    except FileNotFoundError:
        print("Archivo no encontrado, Por favor revisar la ruta")
    except Exception as e:
        print(f"Ocurrio un error: {e}")


def iniciarlector():
 file_path = obtener_path()
 if file_path:
    leerarchivo(file_path)



