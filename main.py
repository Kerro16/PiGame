import clases.lector
import tkinter as tk
from clases.interfaz import ClaseInterfaz
import clases.interfaz_storage
import clases.globales
import threading
from clases.interfaz_storage import InterfazStorage


#Crera la interfaz de seleccion de juego una vez que cerremos esta interfaz corre el hilo donde empieza a leer el archivo y despues abre la segunda interfaz que cambia de imagenes
#Existe una clase dentro de interfaz que manda el valor del nombre del juego y esque hara el cambio dentro de la clase de juegos por nosotros paran o hacerlo atravez de codigo
if __name__ == "__main__":
    root2 = tk.Tk()
    clases.interfaz_storage.InterfazStorage.interfaz = ClaseInterfaz(root2)
    interfaz = InterfazStorage.interfaz
    interfaz.crear_interfaz_con_botones()
    root2.mainloop()

#Se usa un hilo para que se pueda leer el numero de Pi y dar ls instrucciones mientras la interfaz esta abierta

if clases.globales.mi_variable_global:
  hilo_log = threading.Thread(target=clases.lector.iniciarlector)
  hilo_log.start()

#aqui abrimos la interfaz se defino un root por cada interfaz que queremos abrir.
def main():
    root = tk.Tk()
    clases.interfaz_storage.InterfazStorage.interfaz = ClaseInterfaz(root)
    interfaz3= InterfazStorage.interfaz
   # interfaz3.interfazdeNumeroGigante(root3)
    root.mainloop()


if __name__ == "__main__":
    main()





