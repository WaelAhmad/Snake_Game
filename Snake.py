import random
import pygame

class goal:
    def __init__(self):
        self.x = 1
        self.y = 1

    def get_position(self, position):
        self.x = random.randint(0, 390)
        self.y = random.randint(0, 290)
        while self.x % 10 != 0:
            ## update x dimension
            self.x = random.randint(0, 390)
        while self.y % 10 != 0:
            ## update y dimension
            self.y = random.randint(0, 290)
        for i in position:
            if i == (self.x, self.y):
                ## snake reach goal
                self.get_position(position)
                break
    def position(self):
        return (self.x, self.y)
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(self.x, self.y, 10, 10))
class snake:
    def __init__(self, init_pos = (0, 0), dimension = (), snake_size = 1):
        self.position = None
        self.dimension = dimension
        self.init_pos = init_pos
        self.pos = []
        self.pos.append(self.init_pos)

        for i in range(0, snake_size):
            self.pos.append((self.init_pos[0] + len(self.pos) * 10, self.init_pos[1]))

    def eating(self, x, y):
        for i in range(0, 5):
            self.pos = [(x, y)] + self.pos

    def head(self, x = 0, y = 0):
        self.pos[0] = ((self.pos[0][0] + x) % self.dimension[0], (self.pos[0][1] + y) % self.dimension[1])

    def tail(self):
        new_pos = []
        new_pos.append(self.pos[0])
        for i in range(1, len(self.pos)):
            new_pos.append(self.pos[i-1])
        self.pos = new_pos

    def draw(self, screen, color):
        for i in self.pos:
            pygame.draw.rect(screen, color, pygame.Rect(i[0], i[1], 10, 10))

pygame.init()
game_over = False
up = False
down = False
right = False
left = False
goal_reach = False
g = goal()
s = snake(dimension=(400, 300))
g.get_position(s.pos)
DONE = False
color = (0, 128, 255)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 300))
font = pygame.font.SysFont('Comic Sans MS', 20)
text_surface = font.render('0', False, (255, 255, 255))

while not DONE and not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True
    click = pygame.key.get_pressed()
    if click[pygame.K_UP] and not down:
        up = True
        down = False
        right = False
        left = False
    if click[pygame.K_DOWN] and not up:
        up = False
        down = True
        right = False
        left = False
    if click[pygame.K_RIGHT] and not left:
        up = False
        down = False
        right = True
        left = False
    if click[pygame.K_LEFT] and not right:
        up = False
        down = False
        right = False
        left = True

    if up:
        s.head(y=-10)
        s.tail()
    if down:
        s.head(y=10)
        s.tail()
    if right:
        s.head(x=10)
        s.tail()
    if left:
        s.head(x=-10)
        s.tail()
    screen.fill((0, 0, 0))
    text_surface = font.render(str(len(s.pos)-2), False, (255, 255, 255))
    screen.blit(text_surface, (0, 0))
    if s.pos[0] == g.position():
        goal_reach = True
    for i in range(1, len(s.pos)):
        if s.pos[0] == s.pos[i]:
            game_over = True
            print 'GAME OVER !!!'
            break
    if goal_reach:
        s.eating(g.position()[0], g.position()[1])
        g.get_position(s.pos)
        goal_reach = False

    g.draw(screen)
    s.draw(screen, color)
    pygame.display.flip()
    clock.tick(15)
