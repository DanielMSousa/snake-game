import pygame, sys

pygame.init()
from random import randint

#player interaction, level, score and game config
class Game:
    def __init__(self):
        self.clock  = pygame.time.Clock()
        self.font_config = pygame.font.SysFont('arial', 40, True, True)
        self.start_game()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Snake game')

    def start_game(self):
        self.score = 0
        self.weight = 5
        self.obs_list = []
        self.player = Snake()
        self.apple = Apple()
    
    def loop(self):
        while True:
            self.play()

    def check_teleport(self):
        if(self.player.x >= 780 and self.player.x_dir == 1):
            self.player.x = 20
        if(self.player.x <= 20 and self.player.x_dir == -1):
            self.player.x = 780
        if(self.player.y >= 580 and self.player.y_dir == 1):
            self.player.y = 20
        if(self.player.y <= 20 and self.player.y_dir == -1):
            self.player.y = 580

    def check_collisions(self, visual_snake, visual_apple):
            if(visual_snake.colliderect(visual_apple)):
                self.apple.randomize()
                self.score += 1
                self.player.size += 1

            for obstaculo in self.obs_list:
                if(visual_snake.colliderect(obstaculo)):
                    self.game_over(self.player, self.screen)

            if self.player.body[-(self.player.size + 1) * self.weight:].count(self.player.head) > 1:
                self.game_over()

    def controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #discovers if a moving key is being pressed
            if event.type == pygame.KEYDOWN:
                if(self.player.x_dir == 0):
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.player.x_dir = -1
                        self.player.y_dir = 0
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.player.x_dir = 1
                        self.player.y_dir = 0
                if(self.player.y_dir == 0):
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.player.x_dir = 0
                        self.player.y_dir = -1
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.player.x_dir = 0
                        self.player.y_dir = 1

    def generate_level(self):
        self.screen.fill((255, 255, 255))
        message = f'Pontos: {game.score}'
        text = self.font_config.render(message, True, (0, 0, 0))
        return text
    
    def play(self):
        self.clock.tick(60)
        self.controls()
        
        #draws the level, fills the screen, put the score.
        text = self.generate_level()

        visual_snake = pygame.draw.rect(self.screen, (0, 255, 0), (self.player.x, self.player.y, 20, 20))
        visual_apple = pygame.draw.rect(self.screen, (255, 0, 0), (self.apple.x, self.apple.y, 20, 20))
        
        self.player.walk()
        self.check_collisions(visual_snake, visual_apple)
        self.player.draw_snake(self.screen)
        self.check_teleport()

        self.screen.blit(text, (20, 20))
        pygame.display.update()

    def game_over(self):
        fonte_game_over = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over, aperte espaço para reiniciar'
        texto_game_over = fonte_game_over.render(mensagem, True, (0, 0, 0))
        
        self.player.alive = False
        while not self.player.alive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_SPACE):
                        self.start_game()

            texto_rect = texto_game_over.get_rect()
            texto_rect.center = (400, 300)

            self.screen.fill((255, 255, 255))
            self.screen.blit(texto_game_over, texto_rect)
            pygame.display.update()

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

    def draw_snake(self, screen):
        if(len(self.body) > self.size*game.weight):
            del self.body[0]

        for xey in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (xey[0], xey[1], 20, 20))

game = Game()
game.loop()