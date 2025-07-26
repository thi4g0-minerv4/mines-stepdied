from colorama import Fore
from core.objects.Map import Map
from core.assets.game_assets import game_assets

class Game:
    def __init__(self, difficulty: str = 'custom', auto_clear: bool = True, map: Map = None):
        self.difficulty = difficulty
        self.auto_clear = auto_clear
        if map:
            self.map = map
        else:
            self.map = self.generate_map()
        
    def generate_map(self):
        if self.difficulty.lower() == 'custom':
            xlen = int(input("Type the lenght of X-Axis:    "))
            ylen = int(input("Type the lenght of Y-Axis:    "))
            bombs = int(input("Type the quantity of bombs:    "))
            return Map(xlen, ylen, bombs)
        elif self.difficulty.lower() == 'insane':
            return Map(26, 9, 200, False)
        elif self.difficulty.lower() == 'hard':
            return Map(18, 9, 80, False)
        elif self.difficulty.lower() == 'medium':
            return Map(9, 9, 30, self.auto_clear)
        elif self.difficulty.lower() == 'easy':
            return Map(6, 6, 10, self.auto_clear)
        elif self.difficulty.lower() == 'baby':
            return Map(5, 5, 5, True)
        elif self.difficulty.lower() == 'russian_rolet':
            return Map(3, 3, 8, self.auto_clear)
        
            
    def start_game(self):
        print(game_assets['title'])
        while True:
            print(self.map)

            # Win Verification:
            if self.win_verification():
                self.game_over('win')

            
            pre_input = input(f'\n{Fore.YELLOW} Type the Block that you wanna to active {Fore.RESET} {Fore.MAGENTA}(If you want to flag type FL before, the same to disflag. Ex: FL A1) {Fore.GREEN}(To finish the game type "stop"){Fore.RESET}:  ')
            
            final_input = pre_input.lower().strip().replace(" ", "")

            if final_input == 'stop':
                self.game_over('stopped')
                break
            
            if final_input[:2] == 'fl':
                block = self.map.find_block(final_input[2:])
            else:
                block = self.map.find_block(final_input)

            if not block:
                print(f'\nInvalid Block ({final_input[2:] if final_input[:2] == 'fl' else pre_input})\n')
                continue

            if final_input[:2] == 'fl':
                if not block.active_flag():
                    print("\nThe Block is actived, It can't be flagged. ")
            else:
                if block.flagged:
                    i = input('\nThis Block is actually Flagged, are you sure about active it? (type "yes" to active, type any other thing to dont):   ')
                    if i.lower() != 'yes':
                        continue
                    else:
                        block.active_flag()
                if block.actived:
                    print('\nThis block is already actived.')
                    continue

                block.active()
                if block.bomb:
                    self.game_over('bomb')
                    break
    
    def win_verification(self):
        verify_list = []
        for col in self.map.grid:
            for block in col:
                if block.bomb and block.flagged:
                    verify_list.append(True)
                elif not block.bomb and block.actived:
                    verify_list.append(True)
                else:
                    verify_list.append(False)
            
        return all(verify_list)
    
    def game_over(self, method: str = None):
        total_secure_blocks = self.map.xlen * self.map.ylen - self.map.bombs
        actived_secure_blocks = []
        flagged_bomb_blocks = []
        for col in self.map.grid:
            for block in col:
                if block.actived and not block.bomb:
                    actived_secure_blocks.append(block)
                if block.flagged and block.bomb:
                    flagged_bomb_blocks.append(block)
                block.active()

        print(self.map)

        if method.lower() == 'bomb':
            print('\nBUUMMMMMM! You Died.\n')
        elif method.lower() == 'stopped':
            print('\nYou stopped the game. Game Stats:\n')
        elif method.lower() == 'win':
            print("🏆🏆 -- YOU GOT OUT ALIVE MAN -- 🏆🏆\nNow it's just a matter of dealing with the traumas\n")

        print(f'Total of safe blocks revealed: {len(actived_secure_blocks)}/{total_secure_blocks}\nBombs correctly flagged:  {len(flagged_bomb_blocks)}/{self.map.bombs}\n')