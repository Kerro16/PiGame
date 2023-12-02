import clases.juegos
from clases.juegos import *


def leerarchivo():
    # Cerdo
    # file = open('C:/Users/fas_c/Desktop/pi-billion.txt')
    # R20
    file = open('C:/Users/R20/Desktop/pi-billion.txt')
    archivotxt = file.read()
    file.close()
    print("Ya termine de leer el archivo")
    time.sleep(3)
    for index in range(len(archivotxt)):
        numeroPI = archivotxt[index]
        print(clases.juegos.metalSlug(numeroPI, index))

