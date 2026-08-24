import pygame

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Meu programa pygame')

rodando = True

x = 375
y =  275

while rodando:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((0,0,0))
            
    pygame.draw.rect(tela,(255,0,0),(x,y,50,50))
    pygame.display.flip()

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_d] and x < 750:
        x += 1
    if teclas[pygame.K_a] and x > 0:
        x -= 1
    if teclas[pygame.K_w] and y > 0:
        y -= 1
    if teclas[pygame.K_s] and y < 550:
        y += 1

        

pygame.quit()