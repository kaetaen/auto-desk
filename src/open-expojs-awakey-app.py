#!/usr/bin/python3

import pyautogui
from time import sleep

pyautogui.hotkey('ctrl', 'alt', 't')
sleep(2)
pyautogui.write('cd dev && cd awakey && cd mobile')
pyautogui.press('enter')
pyautogui.write('expo start --tunnel')
pyautogui.press('enter')
sleep(2)
pyautogui.hotkey('ctrl', 'shift', 't')
pyautogui.write('nvim')
pyautogui.press('enter')
