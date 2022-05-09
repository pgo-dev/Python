import pygame

pygame.mixer.init()
pygame.init()
#pygame.mixer.init()
#print(pygame.get_init())

pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()

pygame.event.wait()
