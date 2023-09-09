import random

class GameBoard:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.BOARD = {(X, Y) : 0 for Y in range(height) for X in range(width)}
        self.empty = list(self.BOARD.keys())
        
    def getCellValue(self, X:tuple):
        return self.BOARD[X]
    
    def updateCellValue(self, X:tuple, Val:int=None):
        if Val == None:
            if self.BOARD[X] == 0:
                Val = 1
                self.BOARD[X] = 1
                self.empty.remove(X)
            elif self.BOARD[X] == 1:
                Val = 0
                self.BOARD[X] = 0
                self.empty.append(X)
        elif Val == 0:
            self.BOARD[X] = Val
            self.empty.append(X)
        else:
            self.BOARD[X] = Val
            self.empty.remove(X)
            
    def getEmptySpace(self):
        if self.empty == None:
            return None
        else:
            choice = random.choice(self.empty)
            return choice
        
            
        
        
        