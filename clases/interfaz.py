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
        self.cargar_imagenes()
        self.crear_frame_pack()
        self.crear_frame_grid()
        self.mostrar_imagenes()
        self.crear_interfaz_numero()

    def cargar_imagenes(self):
        self.imagen_paths = [
                "imagenes/arriba.jpg",
                "imagenes/abajo.jpg",
                "imagenes/derecha.jpg",
                "imagenes/izquierda.jpg",
                "imagenes/granada.jpg",
                "imagenes/disparar.jpg",
                "imagenes/enter.jpg"
        ]

        self.imagenes = [Image.open(path).resize((600, 300), Image.Resampling.LANCZOS) for path in self.imagen_paths]
        self.photos = [ImageTk.PhotoImage(imagen) for imagen in self.imagenes]

    def crear_frame_pack(self):
            self.pack_frame = tk.Frame(self.root)
            self.pack_frame.pack()
            self.boton_cerrar = tk.Button(self.pack_frame, text="Cerrar", command=self.cerrar_interfaz)
            self.boton_cerrar.pack()

    def crear_frame_grid(self):
                self.grid_frame = tk.Frame(self.root)
                self.grid_frame.pack()
                self.grid_frame2 = tk.Frame(self.root)
                self.grid_frame2.pack()

    def mostrar_imagenes(self):
            self.labels = []
            for idx, photo in enumerate(self.photos):
                 label = tk.Label(self.grid_frame, image=photo)
                 label.grid(row=0, column=idx)
                 self.labels.append(label)
            self.label = self.labels[0]

            self.imagenes_por_numero = {
                "0": self.photos[0],
                "1": self.photos[1],
                "2": self.photos[2],
                "3": self.photos[3],
                "4": self.photos[4],
                "5": self.photos[5],
                "6": self.photos[6],
                # Agregar para el resto de las imágenes según su número
            }

    def cerrar_interfaz(self):
                        self.root.destroy()
                        sys.exit()

    def crear_interfaz_numero(self):
                            self.root.title("Interfaz con numero")
                            self.root.geometry("650x800")
                            self.canvas = tk.Canvas(self.root, width=600, height=300, bg="orange")
                            self.canvas.pack()
                            self.numero_actual = "Pausa"
                            self.texto_numero = self.canvas.create_text(300, 150, text=str(self.numero_actual),
                                                                        font=("Arial", 110), fill="white")
                            self.create_number_squares()  # Asumiendo que esta función está definida en otro lugar


    #definimos los cuadrados naranjas
    def create_square(self, number, color):
        label = tk.Label(self.grid_frame2, text=str(number), bg=color, width=5, height=2, font=("Arial", 12))
        return


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
        imagen = self.imagenes_por_numero.get(numero)
        if clases.globales.mi_variable_global == "Vampire":
            if numero == "0":
                self.label.config(image=self.imagenes_por_numero.get("0"))
            elif numero == "1":
                self.label.config(image=self.imagenes_por_numero.get("1"))
            elif numero == "2":
                self.label.config(image=self.imagenes_por_numero.get("3"))
            elif numero == "3":
                self.label.config(image=self.imagenes_por_numero.get("2"))
            elif numero == "4":
                self.label.config(image=self.imagenes_por_numero.get("6"))
            elif numero == "5":
                self.label.config(image=self.imagenes_por_numero.get("0"))
            elif numero == "6":
                self.label.config(image=self.imagenes_por_numero.get("1"))
            elif numero == "7":
                self.label.config(image=self.imagenes_por_numero.get("3"))
            elif numero == "8":
                self.label.config(image=self.imagenes_por_numero.get("2"))
            elif numero == "9":
                self.label.config(image=self.imagenes_por_numero.get("6"))

        if clases.globales.mi_variable_global == "MetalSlug":
            if numero == "0":
                self.label.config(image=self.imagenes_por_numero.get("0"))
            elif numero == "1":
                self.label.config(image=self.imagenes_por_numero.get("1"))
            elif numero == "2":
                self.label.config(image=self.imagenes_por_numero.get("3"))
            elif numero == "3":
                self.label.config(image=self.imagenes_por_numero.get("2"))
            elif numero == "4":
                self.label.config(image=self.imagenes_por_numero.get("5"))
            elif numero == "5":
                self.label.config(image=self.imagenes_por_numero.get("4"))
            elif numero == "6":
                self.label.config(image=self.imagenes_por_numero.get("2"))
            elif numero == "7":
                self.label.config(image=self.imagenes_por_numero.get("0"))
            elif numero == "8":
                self.label.config(image=self.imagenes_por_numero.get("2"))
            elif numero == "9":
                self.label.config(image=self.imagenes_por_numero.get("3"))





