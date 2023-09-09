import snake, gameBoard

class apple:
    def __init__(self, pos:tuple):
        self.applePos: tuple = pos
    
    def getApplePos(self):
        return self.applePos
         