import time
import pyautogui
pyautogui.FAILSAFE = False #Elimina un crash por mover el mouse o el teclado a cierta parte

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
        print("Enter automatico por el indice en {}".format(index))
        pyautogui.keyDown('enter')
        time.sleep(1)
        pyautogui.keyUp('enter')
    if numero == "0":
        print("Arriba + Disparar")
        pyautogui.keyDown('up')
        pyautogui.keyDown('a')
        time.sleep(1)
        pyautogui.keyUp('up')
        pyautogui.keyUp('a')
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
        print("Disparar")
        pyautogui.keyDown('a')
        time.sleep(1)
        pyautogui.keyUp('a')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "5":
        print("Granada")
        pyautogui.keyDown('s')
        time.sleep(1)
        pyautogui.keyUp('s')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "6":
        print("Derecha + Disparar")
        pyautogui.keyDown('a')
        pyautogui.keyDown('right')
        time.sleep(1)
        pyautogui.keyUp('right')
        pyautogui.keyUp('a')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "7":
        print("Arriba + Disparo")
        pyautogui.keyDown('up')
        pyautogui.keyDown('a')
        time.sleep(1)
        pyautogui.keyUp('up')
        pyautogui.keyUp('a')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "8":
        print("Salto + Derecha")
        pyautogui.keyDown('d')
        pyautogui.keyDown('right')
        time.sleep(1)
        pyautogui.keyUp('right')
        pyautogui.keyUp('d')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)
    elif numero == "9":
        print("Salto + Izquierda")
        pyautogui.keyDown('d')
        pyautogui.keyDown('left')
        time.sleep(1)
        pyautogui.keyUp('left')
        pyautogui.keyUp('d')
        return "El numero de PI es {} y esta en la posicion {}".format(numero, index)