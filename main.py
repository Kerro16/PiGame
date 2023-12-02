import time
import pyautogui

time.sleep(5)
file = open('C:/Users/fas_c/Desktop/pi-billion.txt')
content = file.read()
file.close()
def switch(numero):

    if numero == "0":
        print("Arriba")
        pyautogui.keyDown('up')
        time.sleep(1)
        pyautogui.keyUp('up')
        return numero
    elif numero == "1":
        print("Abajo")
        pyautogui.keyDown('down')
        time.sleep(1)
        pyautogui.keyUp('down')
        return numero
    elif numero == "2":
        print("Izquierda")
        pyautogui.keyDown('left')
        time.sleep(1)
        pyautogui.keyUp('left')
        return numero
    elif numero == "3":
        print("Derecha")
        pyautogui.keyDown('right')
        time.sleep(1)
        pyautogui.keyUp('right')
        return numero
    elif numero == "4":
        print("Enter")
        pyautogui.keyDown('enter')
        time.sleep(1)
        pyautogui.keyUp('enter')
        return numero
    elif numero == "5":
        print("Izquierda")
        pyautogui.keyDown('left')
        time.sleep(1)
        pyautogui.keyUp('left')
        return numero
    elif numero == "6":
        print("Derecha")
        pyautogui.keyDown('right')
        time.sleep(1)
        pyautogui.keyUp('right')
        return numero
    elif numero == "7":
        print("Arriba")
        pyautogui.keyDown('up')
        time.sleep(1)
        pyautogui.keyDown('up')
        return numero
    elif numero == "8":
        print("Abajo")
        pyautogui.keyDown('down')
        time.sleep(1)
        pyautogui.keyUp('down')
        return numero
    elif numero == "9":
        print("Enter")
        pyautogui.keyDown('enter')
        time.sleep(1)
        pyautogui.keyUp('enter')
        return numero


for numero in range(len(content)):
    numeroPI = content[numero]
    print(switch(numeroPI))