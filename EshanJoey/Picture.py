import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

pygame.draw.rect(screen, (0,0,0), (x-2,y-2,155,155), 1)
