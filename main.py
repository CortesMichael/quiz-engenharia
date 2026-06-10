import pygame
import sys
import funcoes

pygame.init()

LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Quiz Engenharia da Transformação Digital")

COR_FUNDO = (255, 0, 255)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(COR_FUNDO)
    pygame.display.flip()
    
pygame.quit()
sys.exit()