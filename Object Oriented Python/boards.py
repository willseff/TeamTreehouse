class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))
                
class TicTacToe(Board):
    def __init__(width):
        height=width
        super().__init__(width,height)

tttboard=TicTacToe(3)