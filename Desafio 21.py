import pygame
pygame.init()
pygame.mixer.music.load('Desafios/ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()

import time
while pygame.mixer.music.get_busy():
    time.sleep(1)
