##Importa a pasta
import pygame
from random import randint

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green =(0,255,0)
blue =(0,0,255)
##Verificando se a biblioteca iniciou corretamente
try:
    pygame.init()
except:
    print('O moduulo nao foi inicializado')
#declaração dessas variaveis caso use dps
largura= 640
altura = 480
tamanho = 10

relogio= pygame.time.Clock()
## define o tamanho da tela
fundo = pygame.display.set_mode((largura, altura))
imag= pygame.image.load('snake.jpg')
pygame.mixer.music.load('musica.mid')
imag2= pygame.image.load('gameover2.jpg')


#titulo para tela
pygame.display.set_caption('Snake')
font = pygame.font.SysFont(None, 25)
font2 = pygame.font.SysFont(None, 15)
##Definições de função
def texto(msg, cor):
    texto1= font.render(msg, True, cor)
    fundo.blit(texto1, [largura/10, altura/1.5])
def textod(msg, cor):
    texto2 = font2.render(msg, True, cor)
    fundo.blit(texto2, [largura/2, altura/1.1])
def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, green, [XY[0], XY[1], tamanho, tamanho])
def maca(maca_x, maca_y):
    pygame.draw.rect(fundo, red, [maca_x, maca_y, tamanho, tamanho])

def jogo():
    sair = True
    fimdejogo = False
    pos_x = randint(0, 630)/2
    pos_y = randint(0, 470)/2
    maca_x = randint(0, 630) / 2
    maca_y = randint(0, 470) / 2
    speed_x = 0
    speed_y = 0
    speed = 1.5
    CobraXY = []
    Cobracump = 1
    pygame.mixer.music.play()
    #inicia o loop
    while sair:
        while fimdejogo:
         #msg se perder
            fundo.blit(imag2,(0,0))
            texto("Fim de jogo!! Para continuar aperte a tecla espaço ou s para sair",red)
            pygame.display.update()
            pygame.mixer.music.stop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo= False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jogo()
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
 #O loop Infinito (aparece as cordenadas)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
    #pra poder sair do looop
                sair = False
    ## Para mover o quadrado/velocidade


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and speed_x != speed:
                    speed_y = 0
                    speed_x = -speed
                if event.key == pygame.K_RIGHT and speed_x != -speed:
                    speed_y = 0
                    speed_x = speed
                if event.key == pygame.K_UP and speed_y != speed:
                    speed_x = 0
                    speed_y = - speed
                if event.key == pygame.K_DOWN and speed_y != -speed:
                    speed_x = 0
                    speed_y = speed

    #definir uma cor pra tela de fundo
        fundo.blit(imag, (0, 0))
    #juntando a posição inicou com acrescimo da velo
        pos_x += speed_x
        pos_y += speed_y
    # colocando a cobra"

        CobraInicio = []
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        CobraXY.append(CobraInicio)
        cobra(CobraXY)
        if len(CobraXY)>Cobracump:
            del CobraXY[0]
    #Inserindo gameover
        if any(Bloco==CobraInicio for Bloco in CobraXY [:-1]):
            fimdejogo= True
    #Colocando a maca e aupmentando a cobra conforme
        if (-tamanho < pos_x - maca_x < tamanho) and (-tamanho< pos_y - maca_y < tamanho):
            maca_x = randint(0, 630) / 2
            maca_y = randint(0, 470) / 2
            Cobracump += 5
            speed += 0.1
        maca(maca_x, maca_y)
    ##lembrar depois de colocar um botão de velocidade usando ifs

        pygame.display.update()
        relogio.tick(100)
        #if pos_x > largura:
            #pos_x = 0
        #if pos_x < 0:
            #pos_x = 630
        #if pos_y > altura:
            #pos_y = 0
        #if pos_y < 0:
            #pos_y = 470
        if pos_x > largura:
           fimdejogo = True
        if pos_x < 0:
             fimdejogo = True
        if pos_y > altura:
             fimdejogo = True
        if pos_y < 0:
            fimdejogo = True

    #Para sair da tela

jogo()
pygame.quit()
