import pygame
from pygame.locals import *

pygame.init()


running = True

gamewindow = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Corgi Game")
black = (0, 0, 0)
white = (255, 255, 255)
img = pygame.image.load(r"C:\Users\Ondra\AppData\Local\Programs\Python\Python37-32\Programy\Programy\corgi2.jpg")

def sprite(x, y):
    gamewindow.blit(img, (x,y))

x = (800*0.45)
y = (600*0.2)

xchange = 0
ychange = 0
imgspeed = 10

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            xchange = -1
        elif event.key == pygame.K_RIGHT:
            xchange = 1
        elif event.key == pygame.K_DOWN:
            ychange = 1
        elif event.key == pygame.K_UP:
            ychange = -1
            
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            xchange = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            ychange = 0

    x += xchange
    y += ychange



            
    gamewindow.fill(white)
    sprite(x,y)
    pygame.display.update()

pygame.quit()

