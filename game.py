#Player: data relative to the player
#Game: player control and map control

import pygame, sys

pygame.init()
from random import randint

#create the display surface
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake game')

#player interaction, level, score and game config
class Game:
    def __init__(self):
        self.clock  = pygame.time.Clock()
        self.score = 0
        self.weight = 5
        self.font_config = pygame.font.SysFont('arial', 40, True, True)
        self.obs_list = []
    
    def check_teleport(self, player):
        if(player.x >= 780 and player.x_dir == 1):
            player.x = 20
        if(player.x <= 20 and player.x_dir == -1):
            player.x = 780
        if(player.y >= 580 and player.y_dir == 1):
            player.y = 20
        if(player.y <= 20 and player.y_dir == -1):
            player.y = 580

    def check_collisions(self, visual_snake, visual_apple, apple):
            if(visual_snake.colliderect(visual_apple)):
                apple.randomize()
                self.score += 1
                player.size += 1

            for obstaculo in self.obs_list:
                if(visual_snake.colliderect(obstaculo)):
                    game_over()

            if player.body[-player.size * self.weight:].count(player.head) > 1:
                game_over()

    def controls(self, player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #discovers if a moving key is being pressed
            if event.type == pygame.KEYDOWN:
                if(player.x_dir == 0):
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        player.x_dir = -1
                        player.y_dir = 0
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        player.x_dir = 1
                        player.y_dir = 0
                if(player.y_dir == 0):
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        player.x_dir = 0
                        player.y_dir = -1
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        player.x_dir = 0
                        player.y_dir = 1

    def generate_level(self):
        screen.fill((255, 255, 255))
        message = f'Pontos: {game.score}'
        text = self.font_config.render(message, True, (0, 0, 0))
        return text

#Controls the apple behaviour
class Apple:
    def __init__(self):
        self.randomize()
    
    def randomize(self):
        self.x = randint(20, 760)
        self.y = randint(20, 560)

#Controls the snake behaviour
class Snake:
    def __init__(self):
        self.x = 400+20
        self.y = 300-20
        self.speed = 6
        self.x_dir = 0
        self.y_dir = 1
        self.size = 5
        self.alive = True
        self.body = []
        self.head = []

    def walk(self):
        self.head = []
        self.head.append(self.x)
        self.head.append(self.y)
        self.body.append(self.head)

        self.x += self.x_dir * self.speed
        self.y += self.y_dir * self.speed

    def draw_snake(self):
        if(len(self.body) > self.size*game.weight):
            del self.body[0]

        for xey in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (xey[0], xey[1], 20, 20))

game = Game()
player = Snake()
apple = Apple()

def inicia_jogo():
    global game, player, apple

    game = Game()
    player = Snake()
    apple = Apple()


def game_over():
    fonte_game_over = pygame.font.SysFont('arial', 20, True, True)
    mensagem = 'Game over, aperte espaço para reiniciar'
    texto_game_over = fonte_game_over.render(mensagem, True, (0, 0, 0))
    
    player.alive = False
    while not player.alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_SPACE):
                    inicia_jogo()

        texto_rect = texto_game_over.get_rect()
        texto_rect.center = (400, 300)

        screen.fill((255, 255, 255))
        screen.blit(texto_game_over, texto_rect)
        pygame.display.update()

while True:
    game.clock.tick(60)
    game.controls(player)
    
    #draws the level, fills the screen, put the score.
    text = game.generate_level()

    visual_snake = pygame.draw.rect(screen, (0, 255, 0), (player.x, player.y, 20, 20))
    visual_apple = pygame.draw.rect(screen, (255, 0, 0), (apple.x, apple.y, 20, 20))
    
    player.walk()
    game.check_collisions(visual_snake, visual_apple, apple)
    player.draw_snake()
    game.check_teleport(player)

    screen.blit(text, (20, 20))
    pygame.display.update()
