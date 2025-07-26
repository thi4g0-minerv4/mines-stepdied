import random
from core.objects.Block import Block
from core.modules.block_appearence import block_appearence

class Map:
    def __init__(self, xlen: int, ylen: int, bombs: int, auto_clear: bool = True):
        self.xlimit = 26
        self.ylimit = 9

        if (xlen > self.xlimit) or (xlen <= 1):
            raise ValueError(f"Max number column (X) is {self.xlimit} (A-Z) and min is 2.")
        if (ylen > self.ylimit) or (ylen <= 1):
            raise ValueError(f"Max number row (Y) is {self.ylimit} and min is 2.")

        if (0 >= bombs) or (bombs >= xlen * ylen) :
            raise ValueError(f"The number of bombs must be between 1 and {xlen * ylen -1}")

        self.xlen = xlen # Max X
        self.ylen = ylen # Max Y
        self.bombs = bombs # Number of bombs in map
        self.grid = self.generate_grid()

        if auto_clear:
            self.func_auto_clear()
    
    def __str__(self):
        return self.generate_grid_str()
    
    def generate_grid(self) -> list:
        bombs = self.bombs
        blocks = []        
        grid = []

        for x in range(1, self.xlen + 1):
            col = []
            for y in range(1, self.ylen + 1):
                block = Block(x, y, self)

                blocks.append(block)

                col.append(block)
            grid.append(col)
        
        for block in random.sample(blocks, bombs):
            block.bomb = True
        
        return grid


    def generate_grid_str(self) -> str:
        grid_str = '\n'
        for y in reversed(range(self.ylen)):
            for x in range(self.xlen):
                block = self.grid[x][y]
                grid_str += f'| {block_appearence(block)} |'
            grid_str += '\n'
        return grid_str


    def func_auto_clear(self):
        for col in self.grid:
            for block in col:
                if not block.bomb and block.bombs_around() <= 1:
                    block.active()

    def find_block(self, position_str: str):
        for col in self.grid:
            for block in col:
                if block.position_str == position_str.upper():
                    return block

