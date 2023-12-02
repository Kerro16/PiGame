import time
import pyautogui
pyautogui.FAILSAFE = False #Elimina un crash por mover el mouse o el teclado a cierta parte


def presionarBotonDoble(letraUno, letraDos, index,numero, movimiento):
    print("Enter automatico por el indice en {}".format(index))
    pyautogui.keyDown(letraUno)
    pyautogui.keyDown(letraDos)
    time.sleep(1)
    pyautogui.keyUp(letraUno)
    pyautogui.keyUp(letraDos)
    return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
def presionarBotonSencillo(letra, index,numero, movimiento):
    print("Enter automatico por el indice en {}".format(index))
    pyautogui.keyDown(letra)
    time.sleep(1)
    pyautogui.keyUp(letra)
    return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
def enterautomatico(index):
    print("Enter automatico por el indice en {}".format(index))
    pyautogui.keyDown('enter')
    time.sleep(1)
    pyautogui.keyUp('enter')



#Vampire Survivors /arriba, abajo, izquierda, derecha y enter/
def vampire(numero, index):
    if numero == "0":
        print("Arriba")
        pyautogui.keyDown('up')
        time.sleep(1)
        pyautogui.keyUp('up')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "1":
        print("Abajo")
        pyautogui.keyDown('down')
        time.sleep(1)
        pyautogui.keyUp('down')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "2":
        print("Izquierda")
        pyautogui.keyDown('left')
        time.sleep(1)
        pyautogui.keyUp('left')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "3":
        print("Derecha")
        pyautogui.keyDown('right')
        time.sleep(1)
        pyautogui.keyUp('right')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "4":
        print("Enter")
        pyautogui.keyDown('enter')
        time.sleep(1)
        pyautogui.keyUp('enter')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "5":
        print("Izquierda")
        pyautogui.keyDown('left')
        time.sleep(1)
        pyautogui.keyUp('left')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "6":
        print("Derecha")
        pyautogui.keyDown('right')
        time.sleep(1)
        pyautogui.keyUp('right')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "7":
        print("Arriba")
        pyautogui.keyDown('up')
        time.sleep(1)
        pyautogui.keyDown('up')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "8":
        print("Abajo")
        pyautogui.keyDown('down')
        time.sleep(1)
        pyautogui.keyUp('down')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "9":
        print("Enter")
        pyautogui.keyDown('enter')
        time.sleep(1)
        pyautogui.keyUp('enter')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)


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