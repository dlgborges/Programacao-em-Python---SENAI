import pygame
import time

pygame.init()

# configure the display window
screen = pygame.display.set_mode(size=(720,720))
pygame.display.set_caption('Title of the window')
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Exiting')
            run = False

    screen.fill('purple')
    pygame.draw.rect(screen, 'black', (360,360,30,30))
    pygame.draw.arc(screen, 'white', (100,100,100,600), 1.5708, 3.1416)
    pygame.draw.ellipse(screen, (0,153,51), (500,500,100,200))
    pygame.display.flip()
    
# time.sleep(10)

pygame.display.quit()