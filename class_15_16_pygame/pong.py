import pygame

pygame.init()

screen = pygame.display.set_mode(size=(720,720))
pygame.display.set_caption('Pong game - Welcome!')
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Exiting')
            run = False

    screen.fill('purple')
    pygame.draw.circle(screen, 'white', (360,360),45, 45)
    # pygame.draw.arc(screen, 'white', (100,100,100,600), 1.5708, 3.1416)

    pygame.display.update()

pygame.display.quit()