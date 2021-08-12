import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(.25)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - Map Theme.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin (1).wav')

morreu = False
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
x_cobra = int(largura/2)
y_cobra = int(altura/2)
x_maca = randint(40, 600)
y_maca = randint(50, 430)
x_controle = 20
y_controle = 0
pontos = 0
velocidade = 10
fonte = pygame.font.SysFont('gabriola', 40, True, True)
pygame.display.set_caption('Primeiro jogo')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento = 5


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 150, 0), (XeY[0], XeY[1], 20, 20))
def reiniciar():
    global pontos, comprimento, x_cobra, y_cobra, lista_cobra,lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento = 5
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False
while True:
    relogio.tick(velocidade)
    tela.fill((255, 255, 255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
    x_cobra += x_controle
    y_cobra += y_controle

    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))
    cobra = pygame.draw.rect(tela, (0, 150, 0), (x_cobra, y_cobra, 20, 20))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        barulho_colisao.play()
        comprimento += 1
    lista_cabeca = [x_cobra, y_cobra]
    lista_cobra.append(lista_cabeca)
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('Arial', 20, True, True)
        mensagem = 'GAME OVER\naperte R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.type == K_r:
                        reiniciar()
            ret_texto.center = (altura//2, largura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura
    if len(lista_cobra) > comprimento:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (400, 40))
    pygame.display.update()

