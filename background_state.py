import pygame
class Background:  
    def __init__(self): 
        self.background = pygame.image.load("images/background_state.png").convert_alpha() 
        self.background = pygame.transform.scale(self.background,(1000,700)) 
        self.font = pygame.font.SysFont(None, 24)  
        # health bar player
        self.imgplayer =  self.font.render('Player\'s health bar', True, (0,0,0)) 
        self.playerHealth = 10 
        self.health_bar = pygame.Rect(20,20,500,20)
        
        # health bar boss 
        self.imgboss = self.font.render('Boss\'s health bar', True, (255,0,0)) 
        self.bossHealth = 100
        self.boss_bar = pygame.Rect(450,660,500,20) 

        #boss appear 
        self.bossappear = "not appear"

    def draw(self,surface): 
        surface.blit(self.background,(0,0))  
        surface.blit(self.imgplayer,(20,2))
        pygame.draw.rect(surface,(225,0,0),self.health_bar) 
        if self.playerHealth > 0 : 
            pygame.draw.rect(surface,(0,255,0),pygame.Rect(20,20,50*self.playerHealth,20))  
        if self.bossappear == "appear": 
            surface.blit(self.imgboss,(450,640))
            pygame.draw.rect(surface,(255,0,0),self.boss_bar) 
            if self.bossHealth > 0 : 
                pygame.draw.rect(surface,(0,0,0),pygame.Rect(450,660,5*self.bossHealth,20))
