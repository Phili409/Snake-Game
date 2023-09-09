import pygame
import apple, gameBoard, snake



class mainGame:
    def __init__(self):
        self.gameBoard = gameBoard.GameBoard(width= (800 // 20) , height= (600 // 20))
        self.snake = snake.snake(position=(19, 13))
        self.apple = apple.apple(pos=self.gameBoard.getEmptySpace())
        self.score:int = 0

        
    def outOfBounds(self) -> bool:
        return self.snake.head.current not in self.gameBoard.BOARD
    
    def appleEaten(self) -> bool:
        return self.snake.head.current == self.apple.applePos
    
    def spawnApple(self):
        space = self.gameBoard.getEmptySpace()
        self.gameBoard.updateCellValue(X=self.apple.applePos, Val=0)
        self.apple.applePos = space
        self.gameBoard.updateCellValue(X=space, Val=2)

    def win(self) -> bool:
        return len(self.gameBoard.getEmptySpace()) == 0
    
    
    def main(self):
        # Constants
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        CELL_SIZE = 20
        GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
        GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

        # Colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        LAVENDER = (230, 230, 250)

        # Initialize Pygame
        pygame.init()
        window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        clock = pygame.time.Clock()
        
        def drawApple():
            APPLE = self.apple.getApplePos()
            pygame.draw.rect(window, RED, (APPLE[0] * CELL_SIZE, APPLE[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    
        def drawSnek():
            SNEK: list = self.snake.getSnake()
            
            for index, snakePZ in enumerate(SNEK):
                if index == 0:
                    pygame.draw.rect(window, LAVENDER, (snakePZ[0] * CELL_SIZE, snakePZ[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                else:
                    pygame.draw.rect(window, WHITE, (snakePZ[0] * CELL_SIZE, snakePZ[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        tick = 7
        while True:
            self.snake.updateSnakeDirection()
            PREvSNEK:list = self.snake.getSnake()
            self.snake.moveSnake()
            
            if self.appleEaten():
                self.spawnApple()
                self.snake.growSnake()
                tick += 4
                self.score += 1
            
            if self.win():
                print(f"Score: {self.score}")
                return True
            elif self.outOfBounds() or self.snake.selfCollided():
                print(f"Score: {self.score}")
                return False
            
            window.fill(BLACK)
            drawApple()
            drawSnek()
            pygame.display.update()
            clock.tick(tick)
    

if __name__ == "__main__":
    SnakeGame = mainGame()
    GameReturn = SnakeGame.main()
    
    if GameReturn:
        print("WINNER")
    else:
        print("LOOSER")
    