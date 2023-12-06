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

        # Frame para los elementos con pack()
        self.pack_frame = tk.Frame(self.root)
        self.pack_frame.pack()

        #agregamos el boton de cerrar interfaz
        self.boton_cerrar = tk.Button(self.pack_frame, text="Cerrar", command=lambda: [self.root.destroy(), sys.exit()])
        self.boton_cerrar.pack()

        #convertimos a un frame de imagen dentro de la interfaz
        self.photo1 = ImageTk.PhotoImage(self.imagen1)
        self.photo2 = ImageTk.PhotoImage(self.imagen2)
        self.photo3 = ImageTk.PhotoImage(self.imagen3)
        self.photo4 = ImageTk.PhotoImage(self.imagen4)
        self.photo5 = ImageTk.PhotoImage(self.imagen5)
        self.photo6 = ImageTk.PhotoImage(self.imagen6)

        # Frame para los elementos con grid()
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack()
        # Frame para los elementos con grid()
        self.grid_frame2 = tk.Frame(self.root)
        self.grid_frame2.pack()

        #iniciamos la intefaz creando el label
        #self.label = tk.Label(self.root, image=self.photo1)
        #self.label.pack()

        self.label = tk.Label(self.grid_frame, image=self.photo1)
        self.label.grid(row=0, column=0)


        self.root.title("Interfaz con numero")
        # definimos la interfaz que muestra el numero gigante de Pi
        self.root.geometry("650x800")  # Tamaño de la ventana
        self.canvas = tk.Canvas(self.root, width=600, height=300, bg="orange")
        self.canvas.pack()


        self.numero_actual = "Pausa"
        self.texto_numero = self.canvas.create_text(300, 150, text=str(self.numero_actual), font=("Arial", 110),fill="white")
    # con esta clase cambiamos el numero de la interfaz con el numero gigante
        self.create_number_squares()


    #definimos los cuadrados naranjas
    def create_square(self, number, color):
        label = tk.Label(self.grid_frame2, text=str(number), bg=color, width=5, height=2, font=("Arial", 12))
        return label
    #Cuadrado rojo
    def create_square_red(self, number, color):
        label = tk.Label(self.grid_frame2, text=str(number), bg=color, width=10, height=4, font=("Arial", 24))
        return label
    #actualizamos los numeros en los cuadrados
    def update_numbers(self,new_numbers):
        for i, number in enumerate(new_numbers):
            self.squares[i].configure(text=str(number))
    #datos de los cuadrados y creacion de los mismos
    def create_number_squares(self):
        colors = ["orange","red"]
        initial_numbers = list(range(1, 10))

        squares = []
        for i in range(9):
            if(i != 8):
                square = self.create_square(0, colors[0])
                square.grid(row=1, column=i, padx=0, pady=0)
                squares.append(square)
            else:
                square = self.create_square_red(0, colors[1])
                square.grid(row=1, column=i, padx=0, pady=0)
                squares.append(square)

        self.squares = squares


    def cambiar_accion(self, nuevo_numero):
        self.numero_actual = nuevo_numero
        self.canvas.itemconfig(self.texto_numero, text=str(self.numero_actual))


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
    def interfazdeNumeroGigante(self,root):
        self.root3 = root
        self.root3.title("Interfaz con numero")
        # definimos la interfaz que muestra el numero gigante de Pi
        self.root3.geometry("600x300")  # Tamaño de la ventana
        self.canvas = tk.Canvas(self.root3, width=600, height=300, bg="orange")
        self.canvas.pack()

        self.canvas.create_text(300, 150, text="5", font=("Arial", 200), fill="white")

    def cambiar_imagen(self, numero):
        if clases.globales.mi_variable_global == "Vampire":
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

        if clases.globales.mi_variable_global == "MetalSlug":
            if numero == "0":
                self.label.config(image=self.photo1)
            elif numero == "1":
                self.label.config(image=self.photo2)
            elif numero == "2":
                self.label.config(image=self.photo4)
            elif numero == "3":
                self.label.config(image=self.photo3)
            elif numero == "4":
                self.label.config(image=self.photo6)
            elif numero == "5":
                self.label.config(image=self.photo5)
            elif numero == "6":
                self.label.config(image=self.photo3)
            elif numero == "7":
                self.label.config(image=self.photo1)
            elif numero == "8":
                self.label.config(image=self.photo3)
            elif numero == "9":
                self.label.config(image=self.photo4)






