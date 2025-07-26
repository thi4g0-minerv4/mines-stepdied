class Block:
    def __init__(self, x: int, y: int, map: list, bomb: bool = False):
        self.position = (x, y)
        self.map = map
        self.bomb = bomb
        self.actived = False
        self.flagged = False
        self.position_str = self.generate_position_str()
    
    def __repr__(self):
        return f'BLOCK(position: {type(self.position).__name__} = {self.position} | bomb: {type(self.bomb).__name__} = {self.bomb})'
    
    def active(self):
        self.actived = True
        return True
    
    def active_flag(self):
        if not self.actived:
            self.flagged = not self.flagged
            return True
        return False
    
    def generate_position_str(self):
        chars = {str(i): chr(64 + i) for i in range(1, 27)} # {"A": "1", "B": 2 ...}
        
        position_str = chars[str(self.position[0])] + str(self.position[1])
        return position_str


    def bombs_around(self)-> int:
        grid = self.map.grid
        xmax = self.map.xlen
        ymax = self.map.ylen

        blocks_around = []
        for xmod in [-1, 0, +1]:
            for ymod in [-1, 0, +1]:
                if xmod == 0 and ymod == 0:
                    continue

                xindex = self.position[0] + xmod
                yindex = self.position[1] + ymod
                
                if (0 < xindex <= xmax) and (0 < yindex <= ymax):
                    blocks_around.append(grid[xindex - 1][yindex - 1])

        bombs_around = []
        for block in blocks_around:
            bombs_around.append(block.bomb)

        return bombs_around.count(True)

    