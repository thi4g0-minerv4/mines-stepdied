import random


class Block:
    def __init__(self, position: list, bomb: bool, map: list = None, actived: bool = False):
        self.position = position 
        self.bomb = bomb
        self.map = map
        self.actived = actived
        
    
    def activate(self):
        self.actived = True

    def bombs_around(self):
        x = self.position[0]
        self.activate()
        y = self.position[1]

        blocks_around_not_validated = [
            [x -1, y -1],
            [x -1, y],
            [x -1, y +1],
            [x, y -1],
            [x, y +1],
            [x +1, y -1],
            [x +1, y],
            [x +1, y +1],   
        ]
        

        max_value = max([block.position[0] and block.position[1] for block in self.map])

        # 1- pega as posições dos blocos em volta
        blocks_position_around = [block for block in blocks_around_not_validated if block[0] > 0 and block[1] > 0 and block[0] <= max_value and block[1] <= max_value]
        
        # 2- Apartir destas posições busca os objetos desses blocos
        blocks_around = [block for block in self.map if block.position in blocks_position_around]
        
        
        bombs_around = len([block for block in blocks_around if block.bomb == True])
        return bombs_around
        



def generate_map() -> list:
    blocks = [
        
    ]

    x = [1,2,3,4,5,6]
    y = [1,2,3,4,5,6]
    for xcord in x:
        for ycord in y:
            blocks.append(Block([xcord,ycord], bomb= True if random.randint(1,5) == 5 else False))
    
    for block in blocks:
        setattr(block, 'map', blocks)
    return blocks 
    

def find_block(map, position: list) -> Block:
    for block in map:
        if block.position == position:
            return block
        
def format_position(pos_input: str)-> list:
    table = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
    }
    pos_format = pos_input.replace(' ', '').upper()
    
    position = [table[pos_format[0]], int(pos_format[1])]
    return (position, pos_format)

map = generate_map()



map_draw = '''
+-----------------------------+
| A6 | B6 | C6 | D6 | E6 | F6 |
| A5 | B5 | C5 | D5 | E5 | F5 |
| A4 | B4 | C4 | D4 | E4 | F4 |
| A3 | B3 | C3 | D3 | E3 | F3 |
| A2 | B2 | C2 | D2 | E2 | F2 |
| A1 | B1 | C1 | D1 | E1 | F1 |
+-----------------------------+   
'''


def game_run(map):

    input_bloco_position = input('Digite a coordenada do bloco que deseja analisar:    ')

    bloco_position = format_position(input_bloco_position)

    bloco = find_block(map, bloco_position[0])

    if bloco.actived:
        print(f'O bloco {bloco_position[1]} já foi ativado. Em volta dele tem {bloco.bombs_around()} bomba(s)')
        
    else:
        bloco.activate()

    if bloco.bomb:
        print('BUMMM, você pegou uma bomba')
        return
    else:
        print(f'Em volta do bloco {bloco_position[1]} tem {bloco.bombs_around()} bomba(s)')
        game_run(map)


game_run(map)