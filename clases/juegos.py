import time
import pyautogui
pyautogui.FAILSAFE = False #Elimina un crash por mover el mouse o el teclado a cierta parte
from clases.interfaz_storage import InterfazStorage

new_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 9]
cadena_movimientos = []



#Actualizamos el array new_numbers con los numeros nuevos de Pi./
def actualizar_fila(numero):
    for i in range(len(new_numbers) - 1):
        new_numbers[i] = new_numbers[i + 1]
        new_numbers[8] = numero

def actualizar_cadena_movimientos(numero):
    cadena_movimientos.append(numero)
    if cadena_movimientos[2]:
        a= 1

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
    pyautogui.keyDown(letra)
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
    if index%9 == 0:
        enterautomatico(index)
    if numero == "0":
        return  presionarBotonDoble('up', 'a', index,numero,'Arriba + Disparo')
    elif numero == "1":
        return presionarBotonSencillo('down',index,numero,'Abajo')
    elif numero == "2":
        return presionarBotonSencillo('left',index,numero,'Izquierda')
    elif numero == "3":
        return presionarBotonSencillo('right',index,numero,'Derecha')
    elif numero == "4":
        return presionarBotonSencillo('a',index,numero,'Disparar')
    elif numero == "5":
        return presionarBotonSencillo('s',index,numero,'Granada')
    elif numero == "6":
        return presionarBotonDoble('right', 'a', index, numero, 'Derecha + Disparo')
    elif numero == "7":
        return presionarBotonDoble('up', 'a', index, numero, 'Arriba + Disparo')
    elif numero == "8":
        return presionarBotonDoble('d', 'right', index, numero, 'Salto + Derecho')
    elif numero == "9":
        return presionarBotonDoble('d', 'left', index, numero, 'Salto + Izquierda')


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
        return boton_rapido('j', index, numero, 'Enter')
    elif numero == "5":
        return boton_rapido('k', index, numero, 'Arriba')
    elif numero == "6":
        return boton_rapido('l', index, numero, 'Down')
    elif numero == "7":
        return boton_rapido('i', index, numero, 'Izquierda')
    elif numero == "8":
        return boton_rapido('o', index, numero, 'Derecha')
    elif numero == "9":
        return boton_rapido('j', index, numero, 'Enter')

