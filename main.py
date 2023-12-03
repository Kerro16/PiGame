import clases.lector
import tkinter as tk
from clases.interfaz import ClaseInterfaz
import clases.interfaz_storage
import threading


hilo_log = threading.Thread(target=clases.lector.iniciarlector)
hilo_log.start()

def main():
    root = tk.Tk()
    clases.interfaz_storage.InterfazStorage.interfaz = ClaseInterfaz(root)
    root.mainloop()

if __name__ == "__main__":
    main()



#clases.interfaz.prueba()









