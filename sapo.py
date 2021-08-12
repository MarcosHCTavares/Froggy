import pygame
from pygame.locals import *
from sys import exit

pygame.init()
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')


class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('Sprit/attack_1.png'))
        self.sprites.append(pygame.image.load('Sprit/attack_2.png'))
        self.sprites.append(pygame.image.load('Sprit/attack_3.png'))
        self.sprites.append(pygame.image.load('Sprit/attack_4.png'))
        self.sprites.append(pygame.image.load('Sprit/attack_5.png'))
        self.sprites.append(pygame.image.load('Sprit/attack_6.png'))
        self.sprites.append(pygame.image.load('Sprit/attack_7.png'))
        self.sprites.append(pygame.image.load('Sprit/attack_8.png'))
        self.sprites.append(pygame.image.load('Sprit/attack_9.png'))
        self.sprites.append(pygame.image.load('Sprit/attack_10.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        self.animar = False

    def atacar(self):
        self.animar = True

    def update(self):
        if self.animar:
            self.atual += .4
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))


todas = pygame.sprite.Group()
sapo = Sapo()
todas.add(sapo)
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo.atacar()
    todas.draw(tela)
    todas.update()
    pygame.display.flip()
