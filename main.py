import clases.lector
import tkinter as tk
from clases.interfaz import ClaseInterfaz
import clases.interfaz_storage
import threading

#Se usa un hilo para que se pueda leer el numero de Pi y dar ls instrucciones mientras la interfaz esta abierta
hilo_log = threading.Thread(target=clases.lector.iniciarlector)
hilo_log.start()

#aqui abrimos la interfaz
def main():
    root = tk.Tk()
    clases.interfaz_storage.InterfazStorage.interfaz = ClaseInterfaz(root)
    root.mainloop()

if __name__ == "__main__":
    main()










