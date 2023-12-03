import tkinter as tk
from PIL import Image, ImageTk
from PIL import Image, ImageTk



"""class ClaseInterfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Imágenes")

        self.imagen1 = Image.open("imagenes/arriba.png")
        self.imagen2 = Image.open("imagenes/abajo.PNG")

        # Redimensionar las imágenes al mismo tamaño
        self.ancho_deseado = 300  # Modifica el ancho deseado de las imágenes
        self.alto_deseado = 200  # Modifica el alto deseado de las imágenes
        self.imagen1 = self.imagen1.resize((self.ancho_deseado, self.alto_deseado), Image.Resampling.LANCZOS)
        self.imagen2 = self.imagen2.resize((self.ancho_deseado, self.alto_deseado), Image.Resampling.LANCZOS)

        self.photo1 = ImageTk.PhotoImage(self.imagen1)
        self.photo2 = ImageTk.PhotoImage(self.imagen2)

        self.label = tk.Label(root, image=self.photo1)
        self.label.pack()

        # Método para cambiar la imagen según el valor recibido
        def cambiar_imagen(valor):
            if valor == 1:
                self.label.config(image=self.photo1)
            elif valor == 2:
                self.label.config(image=self.photo2)
            # Agrega más condiciones para más valores si es necesario"""


def iniciarinterfaz():
        root = tk.Tk()
        root.title("Visualizador de Imágenes")

        imagen1 = Image.open("imagenes/arriba.png")
        imagen2 = Image.open("imagenes/abajo.PNG")

        # Redimensionar las imágenes al mismo tamaño
        ancho_deseado = 300  # Modifica el ancho deseado de las imágenes
        alto_deseado = 200  # Modifica el alto deseado de las imágenes
        imagen1 = imagen1.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)
        imagen2 = imagen2.resize((ancho_deseado, alto_deseado), Image.Resampling.LANCZOS)

        photo1 = ImageTk.PhotoImage(imagen1)
        photo2 = ImageTk.PhotoImage(imagen2)

        label = tk.Label(root, image=photo1)
        label.pack()
        root.mainloop()

"""def iniciarinterfaz():
    foto = Image.open("imagenes/arriba.png")
    root = tk.Tk()
    root.title('Jugando con Pi')
    root.geometry("600x300")
    #root.iconbitmap('/imagenes/arriba')

    #foto = Image.open("imagenes/arriba.jpg")
    #foto = Image.open("imagenes/abajo.PNG")
    resized_image = foto.resize((600,300), Image.Resampling.LANCZOS)
    converted_image = ImageTk.PhotoImage(resized_image)

    label = Label(root, image= converted_image, width=600, height=300, bg="black", fg="yellow")

    label.pack()
    foto = Image.open("imagenes/abajo.PNG")
    foto.save("imagenes/abajo.PNG")
    foto.show()
    label = Label(root, image=converted_image, width=600, height=300, bg="black", fg="yellow")
    label.pack()
    root.mainloop()

def cambiarimagen():
    foto2 = Image.open("imagenes/abajo.PNG")
    resized_image = foto2.resize((600, 300), Image.Resampling.LANCZOS)
    converted_image = ImageTk.PhotoImage(resized_image)

    #label = Label(root, image=converted_image, width=600, height=300, bg="black", fg="yellow")

    #label.pack()"""

"""def prueba():
  window = tk.Tk()
  greeting = tk.Label(text="Hola")
  greeting.pack()
  window.mainloop()"""

