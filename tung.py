import pygame 
pygame.init() 

soze = (800,800) 
screen = pygame.display.set_mode(soze) 
pygame.display.set_caption("Tungggggggggggg") 
image = pygame.image.load("images/boss_game.jpg") 
run = True 
while run:  
    screen.fill((255,255,255))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  
            run = False   
    screen.blit(image,(0,0)) 
    pygame.display.flip()
    