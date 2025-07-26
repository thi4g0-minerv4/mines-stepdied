from colorama import Fore, init
init()

def block_appearence(self) -> str:
        block = self
        if block.actived:
            if block.bomb:
                return Fore.RED + 'XX' + Fore.RESET
            else:
                bombs_around = block.bombs_around()
                text = f'0{bombs_around}'
                if bombs_around <= 0:
                    return Fore.GREEN + text + Fore.RESET
                elif bombs_around <= 1:
                    return Fore.CYAN + text + Fore.RESET
                elif bombs_around <= 2:
                    return Fore.LIGHTYELLOW_EX + text + Fore.RESET
                elif bombs_around <= 5:
                    return Fore.YELLOW + text + Fore.RESET
                elif bombs_around <= 7:
                    return Fore.LIGHTRED_EX + text + Fore.RESET
                elif bombs_around <= 8:
                    return Fore.RED + text + Fore.RESET
        else:
            if block.flagged:
                return Fore.MAGENTA + block.position_str + Fore.RESET
            return block.position_str