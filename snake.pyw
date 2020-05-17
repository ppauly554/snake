import pygame
import collections
import random
pygame.init()

WIDTH = 900
HEIGHT = 900
window = pygame.display.set_mode((WIDTH,HEIGHT))

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                key = pygame.key.name(event.key)
                start = False

class screen:
    def draw():
        global HIGHT, WIDTH
        window.fill((0,0,0))
        for lines in range(WIDTH//100):
            if lines != 0:
                pygame.draw.line(window,(255,255,255),(lines*100,0),(lines*100,HEIGHT))
        for lines in range(HEIGHT//100):
            if lines != 0:
                pygame.draw.line(window,(255,255,255),(0,lines*100),(WIDTH,lines*100))

def keyhandler():
    if key in ("w","a","s","d"):
        if key == "w" and snake.d != 3:
            snake.body.add_value()
            snake.d = 1
        elif key == "a" and snake.d != 2:
            snake.body.add_value()
            snake.d = 4
        elif key == "s" and snake.d != 1:
            snake.body.add_value()
            snake.d = 3
        elif key == "d" and snake.d != 4:
            snake.body.add_value()
            snake.d = 2
    if key == "escape":
        run = False
        pygame.quit()

class snake:
    def __init__(self,x,y,d):
        self.x = x
        self.y = y
        self.d = d
    def move(self):
        if self.d == 1:
            self.y -= 100
            if self.y < 0:
                pygame.quit()
        elif self.d == 2:
            self.x += 100
            if self.x > 800:
                pygame.quit()
        elif self.d == 3:
            self.y += 100
            if self.y > 800:
                pygame.quit()
        elif self.d == 4:
            self.x -= 100
            if self.x < 0:
                pygame.quit()
                
    def draw(self):
        snake = pygame.Surface((100,100))
        snake.fill((0,255,0))
        window.blit(snake, (self.x,self.y))
    class body:
        def add_value():
            movements.appendleft(key)
            if len(movements) > len(body):
                movements.pop()
        def draw():
            bodyx.clear()
            bodyy.clear()
            for parts in range(len(body)):
                if parts == 0:
                    x = snake.x
                    y = snake.y
                if movements[parts] == "w":
                    y += 100
                elif movements[parts] == "a":
                    x += 100
                elif movements[parts] == "s":
                    y -= 100
                elif movements[parts] == "d":
                    x -= 100
                part = pygame.Surface((100,100))
                part.fill((0,255,0))
                window.blit(part,(x,y))
                bodyx.append(x)
                bodyy.append(y)
        def check():
            for (x,y) in zip(bodyx,bodyy):
                if (snake.x,snake.y) == (x,y):
                    pygame.quit()
                    run = False
        def grow():
            movements.append("d")
            body.append(())
class food:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def new(self):
        x = random.randrange(0, 900, 100)
        y = random.randrange(0, 900, 100)
        
        while x in (snake.x, bodyx):
            x = random.randrange(0, 900, 100)
        while y in (snake.y, bodyy):
            y = random.randrange(0, 900, 100)
        self.x = x
        self.y = y
    def check(self):
        if (self.x,self.y) == (snake.x,snake.y):
            snake.body.grow()
            self.new()
    def draw(self):
        food = pygame.Surface((100,100))
        food.fill((255,0,0))
        window.blit(food, (self.x,self.y))

snake = snake(300,400,2)
bodyx = []
bodyy = []
body = []

start_length = 3
body.extend([()]*start_length)

movements = collections.deque(["d"]*start_length)

key = None
i = 0

food = food(500,400)

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)
    pygame.display.flip()
    
    i += 1
    if i == 15:
        i = 0
        if key != None:
            keyhandler()
            
        screen.draw()
        snake.move()
        snake.draw()
        snake.body.draw()
        food.draw()
        
        snake.body.check()
        food.check()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
