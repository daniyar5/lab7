import pygame
import os
from datetime import datetime
pygame.init()

screen = pygame.display.set_mode((800, 600))
done = False

clock = pygame.time.Clock()

_image_library = dict()
def load_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

#images
mainclock = load_image("clocks/mainclock.png")
leftarm = load_image("clocks/leftarm.png")
rightarm = load_image("clocks/rightarm.png")

#controlling size of images
mainclock_new = pygame.transform.scale(mainclock, (800, 600))
leftarm_new = pygame.transform.scale(leftarm, (36, 600))
rightarm_new = pygame.transform.scale(rightarm, (800, 600))

#rectangles
mainclock_r = mainclock_new.get_rect(center = (400, 300))
leftarm_r = leftarm_new.get_rect(center = (400, 300))
rightarm_r = rightarm_new.get_rect(center = (400, 300))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    

    #our time now
    now = datetime.now().time()


    #angles
    angle_la = now.second * 6
    angle_ra = now.minute * 30


    #rotated images
    rotated_la = pygame.transform.rotate(leftarm_new, -angle_la) 
    rotated_ra = pygame.transform.rotate(rightarm_new, -angle_ra) 
 

    #changed rectangles of already rotated images 
    leftarm_r = rotated_la.get_rect(center = mainclock_r.center) 
    rightarm_r = rotated_ra.get_rect(center = mainclock_r.center) 


    #after 60s, turn minute arrow and draw it
    if angle_la == 360:
        rightarm_new = rotated_ra
        screen.blit(rotated_ra, rightarm_r)


    #fill the screen with white color
    screen.fill((255, 255, 255))


    #draw our maicnlock, rotated images and their already changed rectangles
    screen.blit(mainclock_new, mainclock_r) 
    screen.blit(rotated_la, leftarm_r) 
    screen.blit(rotated_ra, rightarm_r) 
    pygame.display.flip() 
    clock.tick(60)























    # screen.fill((255, 255, 255))


    # screen.blit(pygame.transform.scale(load_image("mainclock.png"), (800, 600)), (x, y))
    # screen.blit(pygame.transform.scale(load_image("leftarm.png"), (36, 600)), (390, 0))
    # screen.blit(pygame.transform.scale(load_image("rightarm.png"), (800, 600)), (x, y))



    # pygame.display.flip()
    # clock.tick(60)

