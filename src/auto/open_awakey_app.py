import pyautogui as a # 'a' for automation. Low code XD
from time import sleep

def acess_proj_folder(folder: str):
    proj_path = f'cd dev && cd awakey && cd {folder}'
    a.hotkey('ctrl', 'alt', 't')
    sleep(3)
    a.write(proj_path)
    a.press('enter')


def run_expo_and_neovim():
    acess_proj_folder('mobile')
    a.write('expo start --tunnel')
    a.press('enter')
    sleep(3)
    a.hotkey('ctrl', 'shift', 't')
    a.write('nvim')
    a.press('enter')


def run_api():
    acess_proj_folder('backend')
    a.write('adonis serve --dev')
    a.press('enter')

