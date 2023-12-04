# interfaz.py
import tkinter as tk
from PIL import Image, ImageTk
import clases.globales
import sys
class ClaseInterfaz:
    def __init__(self, root):
        #root crea el frame o la interfaz
        self.root = root
        self.root.title("Interfaz con imagen")
        #llenamos las rutas con los nombres de las imagenes
        self.imagen1 = Image.open("imagenes/arriba.jpg")  # Ruta de la imagen 1
        self.imagen2 = Image.open("imagenes/abajo.PNG")  # Ruta de la imagen 2
        self.imagen3 = Image.open("imagenes/derecha.jpg")  # Ruta de la imagen 3
        self.imagen4 = Image.open("imagenes/izquierda.jpg")  # Ruta de la imagen 4
        self.imagen5 = Image.open("imagenes/granada.png")  # Ruta de la imagen 5
        self.imagen6 = Image.open("imagenes/disparar.jpg")  # Ruta de la imagen 6

        # Redimensionar las imágenes al tamaño deseado (600x300)
        ancho_deseado = 600
        alto_deseado = 300
        self.imagen1 = self.imagen1.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)
        self.imagen2 = self.imagen2.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)
        self.imagen3 = self.imagen3.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)
        self.imagen4 = self.imagen4.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)
        self.imagen5 = self.imagen5.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)
        self.imagen6 = self.imagen6.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)

        #agregamos el boton de cerrar interfaz
        self.boton_cerrar = tk.Button(self.root, text="Cerrar", command= lambda: [self.root.destroy(), sys.exit()])
        self.boton_cerrar.pack()

        #convertimos a un frame de imagen dentro de la interfaz
        self.photo1 = ImageTk.PhotoImage(self.imagen1)
        self.photo2 = ImageTk.PhotoImage(self.imagen2)
        self.photo3 = ImageTk.PhotoImage(self.imagen3)
        self.photo4 = ImageTk.PhotoImage(self.imagen4)
        self.photo5 = ImageTk.PhotoImage(self.imagen5)
        self.photo6 = ImageTk.PhotoImage(self.imagen6)

        #iniciamos la intefaz creando el label
        self.label = tk.Label(self.root, image=self.photo1)
        self.label.pack()

    #Con esta clase que se llama cuando presionamos los bonotes de la primera interfaz llenamos el valor de la variable globlal mi_variable_global
    def enviar_nombre(self, nombre):
        clases.globales.mi_variable_global = nombre
        print(f"Nombre enviado: {clases.globales.mi_variable_global}")


    #Con esta clase podemos crear una interfaz con los botones, al precionar uno le mandaremos ese valor a la clase enviar_nombre
    def crear_interfaz_con_botones(self):
        # Aquí agrega el código para crear los botones y su funcionalidad
        frame = tk.Frame(self.root)
        frame.pack()

        metal_slug_btn = tk.Button(frame, text="MetalSlug", command=lambda: [self.enviar_nombre("MetalSlug"),self.root.destroy()])
        metal_slug_btn.pack(side=tk.LEFT, padx=10, pady=20)

        vampire_btn = tk.Button(frame, text="Vampire", command=lambda: [self.enviar_nombre("Vampire"),self.root.destroy()])
        vampire_btn.pack(side=tk.LEFT, padx=10, pady=20)


      # Se manda llamar esta funcion dependio el numero que le mandemos desde juegos.py sera la imagen que muestre en la interfaz

    def cambiar_imagen2(self, numero):
        if numero == "0":
            self.label.config(image=self.photo1)
        elif numero == "1":
            self.label.config(image=self.photo2)
        elif numero == "2":
            self.label.config(image=self.photo4)
        elif numero == "3":
            self.label.config(image=self.photo3)
        elif numero == "5":
            self.label.config(image=self.photo4)
        elif numero == "6":
            self.label.config(image=self.photo3)
        elif numero == "7":
            self.label.config(image=self.photo1)
        elif numero == "8":
            self.label.config(image=self.photo2)
        elif numero == "9":
            self.label.config(image=self.photo5)



    def cambiar_imagen(self, numero):
        if numero == "0":
            self.label.config(image=self.photo1)
        elif numero == "1":
            self.label.config(image=self.photo2)
        elif numero == "2":
            self.label.config(image=self.photo4)
        elif numero == "3":
            self.label.config(image=self.photo2)
        elif numero == "4":
            self.label.config(image=self.photo5)
        elif numero == "5":
            self.label.config(image=self.photo6)
        elif numero == "6":
            self.label.config(image=self.photo3)
        elif numero == "7":
            self.label.config(image=self.photo1)
        elif numero == "8":
            self.label.config(image=self.photo3)
        elif numero == "9":
            self.label.config(image=self.photo4)