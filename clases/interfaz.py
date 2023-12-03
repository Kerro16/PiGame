# interfaz.py
import tkinter as tk
from PIL import Image, ImageTk

class ClaseInterfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz con imagen")

        self.imagen1 = Image.open("imagenes/arriba.jpg")  # Ruta de la imagen 1
        self.imagen2 = Image.open("imagenes/abajo.PNG")  # Ruta de la imagen 2
        self.imagen3 = Image.open("imagenes/derecha.jpg")
        self.imagen4 = Image.open("imagenes/izquierda.jpg")

        # Redimensionar las imágenes al tamaño deseado (600x300)
        ancho_deseado = 600
        alto_deseado = 300
        self.imagen1 = self.imagen1.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)
        self.imagen2 = self.imagen2.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)
        self.imagen3 = self.imagen3.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)
        self.imagen4 = self.imagen4.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)

        self.photo1 = ImageTk.PhotoImage(self.imagen1)
        self.photo2 = ImageTk.PhotoImage(self.imagen2)
        self.photo3 = ImageTk.PhotoImage(self.imagen1)
        self.photo4 = ImageTk.PhotoImage(self.imagen2)

        self.label = tk.Label(self.root, image=self.photo1)
        self.label.pack()

    def cambiar_imagen(self, numero):
        if numero == "0":
            self.label.config(image=self.photo1)
        elif numero == "1":
            self.label.config(image=self.photo2)
        elif numero == "2":
            self.label.config(image=self.photo4)
        elif numero == "3":
            self.label.config(image=self.photo2)
        elif numero == "6":
            self.label.config(image=self.photo3)
        elif numero == "7":
            self.label.config(image=self.photo1)
        elif numero == "8":
            self.label.config(image=self.photo3)
        elif numero == "9":
            self.label.config(image=self.photo4)
        # Agregar más condiciones según sea necesario para más números
