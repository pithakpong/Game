import pygame 
class Sword : 
    def __init__(self,x,y,surface): 
        self.x = x 
        self.y = y 
        self.surface = surface 
        self.hitboxes = (self.x,self.y,65,50) 
        self.getsword = False
        self.swordimg = pygame.transform.scale(pygame.image.load("images/sword.png"),(65,50)) 
    def draw(self):  
        self.hitboxes = (self.x,self.y,65,50) 
        #pygame.draw.rect(self.surface,(0,0,0),self.hitboxes,1) 
        self.surface.blit(self.swordimg,(self.x,self.y))