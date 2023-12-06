# interfaz.py
import tkinter as tk
from PIL import Image, ImageTk
import clases.globales

class ClaseInterfaz:
    def __init__(self, root):
        #root crea el frame o la interfaz
        self.root = root
        self.root.protocol('WM_DELETE_WINDOW', self.cerrar_hilo)
        self.root.title("Interfaz con imagen")
        self.cargar_imagenes()
        self.crear_frame_pack()
        self.crear_frame_grid()
        self.mostrar_imagenes()
        self.crear_interfaz_numero()

    #Se cargan todas las imagenes en la biblioteca
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
        #Se define como se quiere que se vea la imagen
        self.imagenes = [Image.open(path).resize((600, 300), Image.Resampling.LANCZOS) for path in self.imagen_paths]
        self.photos = [ImageTk.PhotoImage(imagen) for imagen in self.imagenes]

    #Se crea un frame para poder guardar ahi el boton se usa pack
    def crear_frame_pack(self):
            self.pack_frame = tk.Frame(self.root)
            self.pack_frame.pack()

    #se crea un frame para tener las imagenes y los cuadros se usa grid
    def crear_frame_grid(self):
                self.cuadro_numero_index()
                self.grid_frame = tk.Frame(self.root)
                self.grid_frame.pack()
                self.grid_frame2 = tk.Frame(self.root)
                self.grid_frame2.pack()


    #Se muestra aqui la imagene (por el for se muestran todas por ahora pero sin el for no tenemos label para poder usar la funcion de cambiar_imagen
    def mostrar_imagenes(self):
            self.labels = []
            for idx, photo in enumerate(self.photos):
                 label = tk.Label(self.grid_frame, image=photo)
                 label.grid(row=0, column=idx)
                 self.labels.append(label)
            self.label = self.labels[0]
            #ya con el label solo hay que darles un numero de foto que coincida con su posicion en la biblioteca de imagen_paht.
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

    #Aqui se crea la interfz que crea el mensaje de la accion dice numero pq antes mostraba un numero jeje salu2
    def crear_interfaz_numero(self):
                            self.root.title("Interfaz con numero")
                            self.root.geometry("600x900")
                            self.canvas = tk.Canvas(self.root, width=600, height=300, bg="#ffd166")
                            self.canvas.pack()
                            self.numero_actual = "Pausa"
                            self.texto_numero = self.canvas.create_text(300, 150, text=str(self.numero_actual),
                                                                        font=("Roboto", 110), fill="#073b4c")
                            self.create_number_squares()  # Asumiendo que esta función está definida en otro lugar


    #definimos los cuadrados naranjas
    def create_square(self, number, color):
        label = tk.Label(self.grid_frame2, text=str(number), bg=color, width=5, height=2, font=("Roboto", 12))
        return label


    #Cuadrado rojo
    def create_square_red(self, number, color):
        label = tk.Label(self.grid_frame2, text=str(number), bg=color, width=10, height=4, font=("Roboto", 24))
        return label

    def cuadro_numero_index(self):
        self.canvaso = tk.Canvas(self.root, width=600, height=80, bg="#8fd8a0")  # Canvas de 600x100, fondo verde claro
        self.canvaso.pack()
        self.numero_actual = "Han pasado 0 números de Pi"
        self.texto_index = self.canvaso.create_text(300, 40, text=str(self.numero_actual),
                                                    font=("Roboto", 30), fill="#073b4c", anchor="center")

    #actualizamos los numeros en los cuadrados
    def update_numbers(self,new_numbers):
        for i, number in enumerate(new_numbers):
            self.squares[i].configure(text=str(number))


    #datos de los cuadrados y creacion de los mismos
    def create_number_squares(self):
        colors = ["#8fd8a0","#ff6b6b"]
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

    #aqui se cambia la accion en el cuadro gigante y el numero del index hasta arriba
    def cambiar_accion(self, nueva_accion, nueva_index):
        self.accion_actual = nueva_accion
        self.canvas.itemconfig(self.texto_numero, text=str(self.accion_actual))
        self.nueva_index = nueva_index
        self.canvaso.itemconfig(self.texto_index, text="Han pasado {} números de Pi".format(str(self.nueva_index)))


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

    def cerrar_hilo(self):
        clases.globales.mi_variable_global = "Cerrar"
        print("Cerrando aplicacion")
        self.root.destroy()




