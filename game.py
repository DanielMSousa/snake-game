import pygame, sys

pygame.init()
clock = pygame.time.Clock()
from random import randint

#create the display surface
screen = pygame.display.set_mode((800, 600))

x_cobra = 400+20
y_cobra = 300-20

x_maca = randint(20, 760)
y_maca = randint(20, 560)
speed = 3

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

x_dir = 0
y_dir = 1

lista_cobra = []
tamanho_cobra = 5
viva = True

def aumenta_cobra(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(screen, (0, 255, 0), (xey[0], xey[1], 20, 20))

def inicia_jogo():
    global x_cobra, y_cobra, x_maca, y_maca, speed, pontos, tamanho_cobra, lista_cobra, lista_cabeca, viva
    x_maca = randint(20, 760)
    y_maca = randint(20, 560)

    x_cobra = 400+20
    y_cobra = 300-20
    pontos = 0
    tamanho_cobra = 5
    lista_cobra = []
    lista_cabeca = []
    x_dir = 0
    y_dir = 1
    viva = True

def game_over():
    global viva
    fonte_game_over = pygame.font.SysFont('arial', 20, True, True)
    mensagem = 'Game over, aperte espaço para reiniciar'
    texto_game_over = fonte_game_over.render(mensagem, True, (0, 0, 0))
    
    viva = False
    while not viva:
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
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #descobre se uma tecla está sendo pressionada
    
        if event.type == pygame.KEYDOWN:
            if(x_dir == 0):
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x_dir = -1
                    y_dir = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x_dir = 1
                    y_dir = 0
            if(y_dir == 0):
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    x_dir = 0
                    y_dir = -1
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    x_dir = 0
                    y_dir = 1
    #preenche a tela com alguma cor
    #Tem que sempre preencher senão vai ser possível ver a trajetória do objeto.
    #Ou seja é essencial para gerar sensação de movimento
    #ou usa um fill ou cria uma Surface
    screen.fill((255, 255, 255))
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, True, (0, 0, 0))

    #pygame.font.get_fonts() - retorna uma lista todas as fontes disponíveis no sistema.

    cobra = pygame.draw.rect(screen, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(screen, (255, 0, 0), (x_maca, y_maca, 20, 20))

    obs_list = []

    
    if(cobra.colliderect(maca)):
        x_maca = randint(20, 760)
        y_maca = randint(20, 560)
        pontos += 1
        tamanho_cobra += 5

    for obstaculo in obs_list:
        if(cobra.colliderect(obstaculo)):
            game_over()

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if lista_cobra[-tamanho_cobra:].count(lista_cabeca) > 1:
        game_over()

    x_cobra += x_dir * speed
    y_cobra += y_dir * speed

    if(len(lista_cobra) > tamanho_cobra):
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    if(x_cobra >= 780 and x_dir == 1):
        x_cobra = 20
    if(x_cobra <= 20 and x_dir == -1):
        x_cobra = 780
    if(y_cobra >= 580 and y_dir == 1):
        y_cobra = 20
    if(y_cobra <= 20 and y_dir == -1):
        y_cobra = 580

    screen.blit(texto, (20, 20))
    pygame.display.update()



#2 problemas
#Falta de grade
#Comida pode aparecer embaixo da cobra