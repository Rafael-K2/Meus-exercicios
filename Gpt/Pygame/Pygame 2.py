import pygame
import random

pygame.init()
tela = pygame.display.set_mode((800,600))

rodando = True
x = 375
y = 275

velocidade = 1
jogador = pygame.Rect(x, y, 50, 50)

alvo_ativo = True
alvo = pygame.Rect(random.randint(0,770),random.randint(0,570), 30,30)

pontos = 0
while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((0,0,0))

    pygame.draw.rect(tela, (255,0,0), jogador)
    
    if alvo_ativo:
        pygame.draw.rect(tela,(255 ,255 ,0), alvo)

        if jogador.colliderect(alvo):
            pontos += 1
            print(f'Você tem {pontos} pontos!')
            alvo.x = random.randint(0,770)
            alvo.y = random.randint(0,570)

    tecla = pygame.key.get_pressed()

    if tecla[pygame.K_w]:
        jogador.y -= velocidade

    if tecla[pygame.K_s]:
        jogador.y += velocidade

    if tecla[pygame.K_a]:
        jogador.x -= velocidade

    if tecla[pygame.K_d]:
        jogador.x += velocidade

    jogador.x = max(0, min(750, jogador.x))
    jogador.y = max(0, min(550, jogador.y))

    pygame.display.flip()