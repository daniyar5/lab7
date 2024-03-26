import pygame
import os

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

red = (255, 0, 0)
white = (255, 255, 255)

done = False

x = 25
y = 25
radius = 25


clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 20
            elif event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_DOWN:
                y += 20
            if event.key == pygame.K_UP:
                y -= 20


    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_RIGHT]: 
    #     x += 20
    # if keys[pygame.K_LEFT]: 
    #     x -= 20
    # if keys[pygame.K_DOWN]:
    #     y += 20
    # if keys[pygame.K_UP]:
    #     y -= 20

    if x < radius:
        x = radius
    elif x > width - radius:
        x = width - radius
    if y < radius:
        y = radius
    elif y > height - radius:
        y = height - radius

    screen.fill(white)

    
    pygame.draw.circle(screen, red, (x, y), radius)

    pygame.display.flip()
    clock.tick(60)