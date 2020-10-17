import pyautogui
from time import sleep

pyautogui.moveTo(8, 8)
pyautogui.click()
pyautogui.write('terminal')
pyautogui.press('ENTER')
sleep(4)
pyautogui.write('cd dev && cd awakey && cd mobile')
pyautogui.press('ENTER')
pyautogui.write('expo start --tunnel')
pyautogui.press('ENTER')
pyautogui.keyDown('CTRL')
pyautogui.keyDown('SHIFT')
pyautogui.press('t')
pyautogui.keyUp('CTRL')
pyautogui.keyUp('SHIFT')
sleep(4)
pyautogui.write('nvim')
pyautogui.press('ENTER')


