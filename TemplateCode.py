#import and init pygame library
import pygame
pygame.init()

#set up drawing window (this will just make a screen flash on)
screen = pygame.display.set_mode([800, 600])

#run until user asks to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #time for the actual game
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,255), (250,250), 75)
    
    
    #have to have this at the end to display
    pygame.display.update()

pygame.quit()

