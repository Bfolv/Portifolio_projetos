import pyautogui
import time

pyautogui.alert('o codigo vai começar. Não use o nada do seu computador ate finalizar a tarefa')
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/home')
pyautogui.press('enter')

pyautogui.hotkey('winleft', 'd')

pyautogui.moveTo(1865,  669)
pyautogui.mouseDown()
pyautogui.moveTo(417, 515)

pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.mouseUp()

pyautogui.alert('O programa terminou de rodar, ja pode utilizar ^^')