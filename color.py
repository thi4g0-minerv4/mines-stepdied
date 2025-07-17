import time

from colorama import init, Back, Fore
from core.assets import ascii_start

init(autoreset=False)

cores_back = {
    'yellow': Back.YELLOW,
    'green': Back.GREEN,
    'white': Back.WHITE,
    'magenta': Back.MAGENTA,
    'black': Back.BLACK,
    'red': Back.RED,
    'blue': Back.BLUE
}

cores_font = {
    'yellow': Fore.YELLOW,
    'green': Fore.GREEN,
    'white': Fore.WHITE,
    'magenta': Fore.MAGENTA,
    'black': Fore.BLACK,
    'red': Fore.RED,
    'blue': Fore.BLUE,
    'reset': Fore.WHITE
}

print(f'{cores_back['black']}{cores_font['red']}{ascii_start}')

time.sleep(0.3)
input(f'{cores_font['yellow']}!!-- Pressione ENTER para iniciar o jogo --!!')