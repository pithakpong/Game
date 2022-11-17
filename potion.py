import pygame 
class Potion: 
    def __init__(self,x,y,surface): 
        self.x = x 
        self.y = y 
        self.surface = surface 
        self.hitboxes = (self.x,self.y,50,50) 
        self.potionimg = pygame.transform.scale(pygame.image.load("images/potion.png"),(50,50)) 
    def draw(self):  
        self.hitboxes = (self.x,self.y,50,50) 
        #pygame.draw.rect(self.surface,(0,0,0),self.hitboxes,1) 
        self.surface.blit(self.potionimg,(self.x,self.y))