import pygame 
pygame.init()   

class Images :  
    def __init__(self): 
        
        # main State
        self.start_img = pygame.image.load("images/start.png").convert_alpha() 
        self.exit_img = pygame.image.load("images/exit.png").convert_alpha() 
        self.background_img = pygame.image.load("images/background.png").convert_alpha()  
        self.bombimg = pygame.transform.scale(pygame.image.load("images/bomb.png"),(35,35)).convert_alpha()
        self.bombeffect = pygame.transform.scale(pygame.image.load("images/bomb_effect.png"),(300,300)).convert_alpha() 

        #game over State 
        self.replay_img = pygame.image.load("images/replay_button.png").convert_alpha() 
        self.quit_img = pygame.image.load("images/quit.png").convert_alpha() 
        self.gameover_img = pygame.image.load("images/gameover.png").convert_alpha()
        self.score_img = pygame.image.load("images/score.png").convert_alpha()
        self.win = pygame.transform.scale(pygame.image.load("images/win.png"),(500,350))