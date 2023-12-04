import time
import pyautogui
pyautogui.FAILSAFE = False #Elimina un crash por mover el mouse o el teclado a cierta parte
from clases.interfaz_storage import InterfazStorage




#Todos los botones hacen un keydown o keyup que es el presionado, el interfaz.cambiar_imagen se usa para cambiar la imagen en la interfaz
def presionarBotonDoble(letraUno, letraDos, index,numero, movimiento):
    print(movimiento)
    pyautogui.keyDown(letraUno)
    pyautogui.keyDown(letraDos)
    time.sleep(1)
    pyautogui.keyUp(letraUno)
    pyautogui.keyUp(letraDos)
    interfaz = InterfazStorage.interfaz
    interfaz.cambiar_imagen(numero)
    return "El numero de PI es {} y esta en la posicion {}".format(numero, index)


def presionarBotonSencillo(letra, index,numero, movimiento):
    print(movimiento)
    pyautogui.keyDown(letra)
    time.sleep(1)
    pyautogui.keyUp(letra)
    interfaz = InterfazStorage.interfaz
    interfaz.cambiar_imagen(numero)
    return "El numero de PI es {} y esta en la posicion {}".format(numero, index)


def enterautomatico(index):
    print("Enter automatico por el indice en {}".format(index))
    pyautogui.keyDown('enter')
    time.sleep(1)
    pyautogui.keyUp('enter')


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
        return presionarBotonSencillo('left',index,numero,'Izquierda')
    elif numero == "6":
        return presionarBotonSencillo('right',index,numero,'Derecha')
    elif numero == "7":
        return presionarBotonSencillo('up',index,numero,'Arriba')
    elif numero == "8":
        return presionarBotonSencillo('down',index,numero,'Abajo')
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
        return presionarBotonDoble('rigth', 'a', index, numero, 'Derecha + Disparo')
    elif numero == "7":
        return presionarBotonDoble('up', 'a', index, numero, 'Arriba + Disparo')
    elif numero == "8":
        return presionarBotonDoble('d', 'right', index, numero, 'Salto + Derecho')
    elif numero == "9":
        return presionarBotonDoble('d', 'left', index, numero, 'Salto + Izquierda')