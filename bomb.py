import pygame 
class Bomb : 
    def __init__(self,surface,posx,posy,turn): 
        self.turn = turn 
        self.surface = surface 
        self.x = posx 
        self.y = posy 
        self.count = 0 
        #self.shoot = "not shoot"
        self.bombimg = pygame.transform.scale(pygame.image.load("images/bomb.png"),(35,35))
        self.bombeffect = pygame.transform.scale(pygame.image.load("images/bomb_effect.png"),(300,300))

    def draw(self): 
        self.hitboxes = (self.x-150,self.y-150,300,300)  
        #if self.shoot == "shoot":
        if  self.x >= 0 and self.x <= 1000 and self.y >= 0 and self.y <= 700:
            self.count += 3  
            if self.turn == "right idle":
                self.surface.blit(self.bombimg,(self.x,self.y)) 
                self.x += 3 
            if self.turn == "left idle":
                self.surface.blit(self.bombimg,(self.x,self.y)) 
                self.x -=3  
        #pygame.draw.rect(self.surface,(0,0,0),self.hitboxes,1)
        if self.count >= 200: 
            return True  
        return False 
    def draweffect(self):
        self.surface.blit(self.bombeffect,(self.x-150,self.y-150)) 
        self.shoot = "not shoot" 


class BombShow: 
    def __init__(self,x,y,surface): 
        self.x = x 
        self.y = y 
        self.surface = surface 
        self.hitboxes = (self.x,self.y,35,35) 
        self.bombimg = pygame.transform.scale(pygame.image.load("images/bomb.png"),(35,35)) 
    def draw(self):  
        self.hitboxes = (self.x,self.y,35,35) 
        #pygame.draw.rect(self.surface,(0,0,0),self.hitboxes,1) 
        self.surface.blit(self.bombimg,(self.x,self.y))