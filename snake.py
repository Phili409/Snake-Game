import pygame

class Node:
    def __init__(self, position):
        self.current = position
        self.nextNode = None

class snake:
    def __init__(self, position:tuple):
        self.head = Node(position)
        self.tail = self.head.nextNode = Node(position=(position[0] + 0, position[1] + 1))
        self.direction = 'N'
        self.directionOffsets = {
            'N' : (0, -1),
            'E' : (1, 0),
            'S' : (0, 1),
            'W' : (-1, 0)
            }
        self.directions = ['N', 'E', 'S', 'W']
        
    def growSnake(self):
        snekTail = self.tail.current
    
        xTAIL, yTAIL = snekTail
        xMove, yMove = self.directionOffsets[self.directions[(self.directions.index(self.direction) + 2) % 4]]    
    
        newTail = (xTAIL + xMove, yTAIL + yMove) 
        newTail = Node(newTail)   
    
        self.tail.nextNode = newTail
        self.tail = newTail
        
        
        
    def selfCollided(self) -> bool:
        if self.head.nextNode == None:
            return False
        snake = self.getSnake()
        head = snake.pop(0)
        return (head in snake)
    
    def removeTail(self):
        currentNode = self.head
        
        while currentNode.nextNode.nextNode:
            currentNode = currentNode.nextNode
        currentNode.nextNode = None
        return currentNode
        
    def moveSnake(self):
        xMove, yMove = self.directionOffsets[self.direction]  
        currentNode = self.head
        xHead, yHead = currentNode.current
        newHEAD = Node((xMove + xHead, yMove + yHead))
        newTail = self.removeTail()
        newBody = self.head
        newHEAD.nextNode = newBody
        self.head = newHEAD
        self.tail = newTail
        
        
    def updateSnakeDirection(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != 'S' and self.direction != 'N':
                    self.direction = 'N'
                elif event.key == pygame.K_DOWN and self.direction != 'N' and self.direction != 'S':
                    self.direction = 'S'
                elif event.key == pygame.K_LEFT and self.direction != 'E' and self.direction != 'W':
                    self.direction = 'W'
                elif event.key == pygame.K_RIGHT and self.direction != 'W' and self.direction != 'E':
                    self.direction = 'E'
    
    def getSnake(self) -> list[tuple]:
        snake = []
        current = self.head
        
        while current:
            snake.append(current.current)
            current = current.nextNode
        return snake