import time

import pyautogui

pi = "3.14159265358971040317211860820419000413375751149595015660235072835049530984448933087807693259939780541934144"
time.sleep(3)

def switch(numero):
    if numero == "0":
        pyautogui.keyDown('up')
        time.sleep(1)
        pyautogui.keyUp('up')
        return "Arriba"
    elif numero == "1":
        pyautogui.keyDown('down')
        time.sleep(1)
        pyautogui.keyUp('down')
        return "Abajo"
    elif numero == "2":
        pyautogui.keyDown('left')
        time.sleep(1)
        pyautogui.keyUp('lef')
        return "Izquierda"
    elif numero == "3":
        pyautogui.keyDown('right')
        time.sleep(1)
        pyautogui.keyUp('right')
        return "Derecha"
    elif numero == "4":
        pyautogui.keyDown('enter')
        time.sleep(1)
        pyautogui.keyUp('enter')
        return "Enter"
    elif numero == "5":
        pyautogui.keyDown('left')
        time.sleep(1)
        pyautogui.keyUp('left')
        return "Izquierda"
    elif numero == "6":
        pyautogui.keyDown('right')
        time.sleep(1)
        pyautogui.keyUp('right')
        return "Derecha"
    elif numero == "7":
        pyautogui.keyDown('up')
        time.sleep(1)
        pyautogui.keyDown('up')
        return "Arriba"
    elif numero == "8":
        pyautogui.keyDown('down')
        time.sleep(1)
        pyautogui.keyUp('down')
        return "Abajo"
    elif numero == "9":
        pyautogui.keyDown('enter')
        time.sleep(1)
        pyautogui.keyUp('enter')
        return "Enter"


for numero in range(len(pi)):
    numeroPI = pi[numero]
    print(switch(numeroPI))





