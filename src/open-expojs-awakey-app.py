#!/usr/bin/python3

import pyautogui
from time import sleep

pyautogui.hotkey('ctrl', 'alt', 't')
sleep(2)
pyautogui.write('cd dev && cd awakey && cd mobile')
pyautogui.press('ENTER')
pyautogui.write('expo start --tunnel')
pyautogui.press('ENTER')
pyautogui.hotkey('ctrl', 'shift', 't')
sleep(1)
pyautogui.write('nvim')
pyautogui.press('ENTER')

