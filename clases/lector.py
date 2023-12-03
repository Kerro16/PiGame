import clases.juegos
from clases.juegos import *
import tkinter as tk
from tkinter import filedialog

#se abre la ruta del archivo
def obtener_path():
    root = tk.Tk()
    root.withdraw()
    file_path =  "C:/Users/R20/Desktop/pi-billion.txt"           #filedialog.askopenfilename(title="Selecciona un archivo")
    return file_path

#Se lee el archivo donde tenemos pi
def leerarchivo(file_path):
    try:
        with open(file_path, 'r') as file:
            archivotxxt = file.read()

            print("Archivo leido exitosamente")
            time.sleep(2)
            #tomamos cada numero de pi y lo mandamos a juegos.py donde lo convierte a inputs de taclado solo es necesario cambiar el clase.juegos.xxx por el deseado
            for index in range(len(archivotxxt)):
                numeroPI = archivotxxt[index]
                print(clases.juegos.metalSlug(numeroPI, index))

    except FileNotFoundError:
        print("Archivo no encontrado, Por favor revisar la ruta")
    except Exception as e:
        print(f"Ocurrio un error: {e}")

#Este se manda llamar para iniciar con la lectura de el archivo.
def iniciarlector():
 file_path = obtener_path()
 if file_path:
    leerarchivo(file_path)



