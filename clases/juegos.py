import time
import pyautogui

import clases.globales

pyautogui.FAILSAFE = False #Elimina un crash por mover el mouse o el teclado a cierta parte
from clases.interfaz_storage import InterfazStorage
import random
from clases.globales import posicion_secuencia_botones

new_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 9]
secuencia_botones = ["a","b","c"]




#Actualizamos el array new_numbers con los numeros nuevos de Pi./
def actualizar_fila(numero):
    for i in range(len(new_numbers) - 1):
        new_numbers[i] = new_numbers[i + 1]
        new_numbers[8] = numero


#Todos los botones hacen un keydown o keyup que es el presionado, el interfaz.cambiar_imagen se usa para cambiar la imagen en la interfaz
def presionarBotonDoble(letraUno, letraDos, index,numero, movimiento):
    print(movimiento)
    interfaz = InterfazStorage.interfaz
    interfaz.cambiar_imagen(numero)
    interfaz.cambiar_accion(movimiento,index)
    actualizar_fila(numero)
    interfaz.update_numbers(new_numbers)
    print("El numero de PI es {} y esta en la posicion {}".format(numero, index))
    pyautogui.keyDown(letraUno)
    pyautogui.keyDown(letraDos)
    time.sleep(1)
    pyautogui.keyUp(letraUno)
    pyautogui.keyUp(letraDos)
    return "pensanding..."

def presionar_boton_triple(letraUno, letraDos,letraTres,index,numero, movimiento):
    print(movimiento)
    interfaz = InterfazStorage.interfaz
    interfaz.cambiar_imagen(numero)
    interfaz.cambiar_accion(movimiento,index)
    actualizar_fila(numero)
    interfaz.update_numbers(new_numbers)
    print("El numero de PI es {} y esta en la posicion {}".format(numero, index))
    pyautogui.keyDown(letraUno)
    pyautogui.keyDown(letraDos)
    pyautogui.keyDown(letraTres)
    time.sleep(1)
    pyautogui.keyUp(letraUno)
    pyautogui.keyUp(letraDos)
    pyautogui.keyUp(letraTres)
    return "pensanding..."


def presionarBotonSencillo(letra, index,numero, movimiento):
    print(movimiento)
    interfaz = InterfazStorage.interfaz
    interfaz.cambiar_imagen(numero)
    interfaz.cambiar_accion(movimiento,index)
    actualizar_fila(numero)
    interfaz.update_numbers(new_numbers)
    print("El numero de PI es {} y esta en la posicion {}".format(numero, index))
    pyautogui.keyDown(letra)
    time.sleep(1)
    pyautogui.keyUp(letra)
    return "pensanding...."


def enterautomatico(index):
    print("Enter automatico por el indice en {}".format(index))
    pyautogui.keyDown('enter')
    time.sleep(1)
    pyautogui.keyUp('enter')


def boton_rapido(letra, index,numero, movimiento):
    print(movimiento)
    interfaz = InterfazStorage.interfaz
    interfaz.cambiar_imagen(numero)
    interfaz.cambiar_accion(movimiento, index)
    actualizar_fila(numero)
    interfaz.update_numbers(new_numbers)
    print("El numero de PI es {} y esta en la posicion {}".format(numero, index))
    if letra == "u":
        numero_aleatorio = random.randint(1, 4)
        if numero_aleatorio == 1:
            pyautogui.keyDown("a")
            pyautogui.keyDown("s")
            pyautogui.keyDown("d")
            pyautogui.keyDown("k")
            time.sleep(0.5)
            pyautogui.keyUp("a")
            pyautogui.keyUp("s")
            pyautogui.keyUp("d")
            pyautogui.keyUp("k")
        elif numero_aleatorio == 2:
            pyautogui.keyDown("d")
            pyautogui.keyDown("s")
            pyautogui.keyDown("a")
            pyautogui.keyDown("k")
            time.sleep(0.5)
            pyautogui.keyUp("d")
            pyautogui.keyUp("s")
            pyautogui.keyUp("a")
            pyautogui.keyUp("k")
        elif numero_aleatorio == 3:
            pyautogui.keyDown("d")
            pyautogui.keyDown("a")
            pyautogui.keyDown("j")
            time.sleep(0.5)
            pyautogui.keyUp("d")
            pyautogui.keyUp("a")
            pyautogui.keyUp("j")
        elif numero_aleatorio == 4:
            pyautogui.keyDown("a")
            pyautogui.keyDown("d")
            pyautogui.keyDown("j")
            time.sleep(0.5)
            pyautogui.keyUp("a")
            pyautogui.keyUp("d")
            pyautogui.keyUp("j")
    else:
        pyautogui.keyDown(letra)
        pyautogui.keyUp(letra)
    return "pensanding...."

def boton_combos_mortal(letra, index,numero, movimiento):
    if  clases.globales.posicion_secuencia_botones == 1:
        clases.globales.posicion_secuencia_botones = 2
        secuencia_botones[0] = letra
    elif clases.globales.posicion_secuencia_botones == 2:
        clases.globales.posicion_secuencia_botones = 3
        secuencia_botones[1] = letra
    elif clases.globales.posicion_secuencia_botones == 3:
        clases.globales.posicion_secuencia_botones = 1
        secuencia_botones[2] = letra
        print(movimiento)
        interfaz = InterfazStorage.interfaz
        interfaz.cambiar_imagen(numero)
        interfaz.cambiar_accion(movimiento, index)
        actualizar_fila(numero)
        interfaz.update_numbers(new_numbers)
        print("El numero de PI es {} y esta en la posicion {}".format(numero, index))
        if letra == "u":
            numero_aleatorio = random.randint(1, 4)
            if numero_aleatorio == 1:
                pyautogui.keyDown("a")
                pyautogui.keyDown("s")
                pyautogui.keyDown("d")
                pyautogui.keyDown("k")
                time.sleep(0.5)
                pyautogui.keyUp("a")
                pyautogui.keyUp("s")
                pyautogui.keyUp("d")
                pyautogui.keyUp("k")
            elif numero_aleatorio == 2:
                pyautogui.keyDown("d")
                pyautogui.keyDown("s")
                pyautogui.keyDown("a")
                pyautogui.keyDown("k")
                time.sleep(0.5)
                pyautogui.keyUp("d")
                pyautogui.keyUp("s")
                pyautogui.keyUp("a")
                pyautogui.keyUp("k")
            elif numero_aleatorio == 3:
                pyautogui.keyDown("d")
                pyautogui.keyDown("a")
                pyautogui.keyDown("j")
                time.sleep(0.5)
                pyautogui.keyUp("d")
                pyautogui.keyUp("a")
                pyautogui.keyUp("j")
            elif numero_aleatorio == 4:
                pyautogui.keyDown("a")
                pyautogui.keyDown("d")
                pyautogui.keyDown("j")
                time.sleep(0.5)
                pyautogui.keyUp("a")
                pyautogui.keyUp("d")
                pyautogui.keyUp("j")
        else:
            pyautogui.keyDown(secuencia_botones[0])
            pyautogui.keyDown(secuencia_botones[1])
            pyautogui.keyDown(secuencia_botones[2])
            time.sleep(0.2)
            pyautogui.keyUp(secuencia_botones[0])
            pyautogui.keyUp(secuencia_botones[1])
            pyautogui.keyUp(secuencia_botones[2])
    return "numero_aleatorio"

def boton_pescar(letra, index,numero, movimiento):
    print(movimiento)
    interfaz = InterfazStorage.interfaz
    interfaz.cambiar_imagen(numero)
    interfaz.cambiar_accion(movimiento,index)
    actualizar_fila(numero)
    interfaz.update_numbers(new_numbers)
    print("El numero de PI es {} y esta en la posicion {}".format(numero, index))
    pyautogui.keyDown(letra)
    time.sleep(3)
    pyautogui.keyUp(letra)
    return "pensanding...."


#Vampire Survivors /arriba, abajo, izquierda, derecha y enter/
def vampire(numero, index):
    if numero == "0":
        return presionarBotonSencillo('up',index,numero,'Arriba')
    elif numero == "1":
        return presionarBotonSencillo('down',index,numero,'Abajo')
    elif numero == "2":
        return presionarBotonSencillo('left',index,numero,'Izquierda')
    elif numero == "3":
        return presionarBotonSencillo('right',index,numero,'Derecha')
    elif numero == "4":
        return presionarBotonSencillo('enter',index,numero,'Enter')
    elif numero == "5":
        return presionarBotonSencillo('up',index,numero,'Arriba')
    elif numero == "6":
        return presionarBotonSencillo('down',index,numero,'Down')
    elif numero == "7":
        return presionarBotonSencillo('left',index,numero,'Izquierda')
    elif numero == "8":
        return presionarBotonSencillo('right',index,numero,'Derecha')
    elif numero == "9":
        return presionarBotonSencillo('enter',index,numero,'Enter')


# Metal Slug /arriba, abajo, izquierda, derecha, a , s , d  se agrega un enter cada que el index pasa por 9 iteraciones/
def metalSlug(numero, index):
    if index%8 == 0:
        enterautomatico(index)
    if numero == "0":
        return  presionarBotonDoble('up', 'a', index,numero,'A+Disparo')
    elif numero == "1":
        return presionarBotonSencillo('down',index,numero,'Abajo')
    elif numero == "2":
        return presionarBotonSencillo('left',index,numero,'Izquierda')
    elif numero == "3":
        return presionarBotonSencillo('right',index,numero,'Derecha')
    elif numero == "4":
        return presionar_boton_triple('d','down','a',index,numero,'D+Abajo')
    elif numero == "5":
        return presionarBotonSencillo('s',index,numero,'Granada')
    elif numero == "6":
        return presionarBotonDoble('right', 'a', index, numero, 'D+Disparo')
    elif numero == "7":
        return presionarBotonDoble('up', 'a', index, numero, 'A+Disparo')
    elif numero == "8":
        return presionarBotonDoble('d', 'right', index, numero, 'S+Derecho')
    elif numero == "9":
        return presionarBotonDoble('d', 'left', index, numero, 'S+Izquierda')


def mortal_kombat(numero, index):
    if numero == "0":
        return boton_rapido('w', index, numero, 'Arriba')
    elif numero == "1":
        return boton_rapido('s', index, numero, 'Abajo')
    elif numero == "2":
        return boton_rapido('a', index, numero, 'Izquierda')
    elif numero == "3":
        return boton_rapido('d', index, numero, 'Derecha')
    elif numero == "4":
        return boton_rapido('j', index, numero, 'Golpe')
    elif numero == "5":
        return boton_rapido('k', index, numero, 'Patada')
    elif numero == "6":
        return boton_rapido('l', index, numero, 'Golpe')
    elif numero == "7":
        return boton_rapido('i', index, numero, 'Golpe')
    elif numero == "8":
        return boton_rapido('o', index, numero, 'Defensa')
    elif numero == "9":
        return boton_rapido('u', index, numero, 'Combo')

def Pesca(numero,index):
    if numero == "0" or numero == "2" or numero == "4" or numero == "6" or numero == "8":
        return boton_pescar('6', index, numero, 'jalar')
    elif numero == "1" or numero == "3" or numero == "5" or numero == "7" or numero == "9":
        return boton_pescar('7', index, numero, 'soltar')

