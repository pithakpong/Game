import pygame 
pygame.init()

class Bullet: 
    def __init__(self,posx,posy,direction,screen,screen_width,mode,checksword):
        self.posx = posx 
        self.posy = posy  
        self.direction = direction 
        self.screen = screen 
        self.screen_width = screen_width 
        #bullet left
        self.bulletimg_left = pygame.image.load("images/buttlet_left.png").convert_alpha() 
        self.bulletimg_left = pygame.transform.scale(self.bulletimg_left,(32,50))   
        #bullet right
        self.bulletimg_right = pygame.image.load("images/buttlet_right.png").convert_alpha() 
        self.bulletimg_right = pygame.transform.scale(self.bulletimg_right,(32,50))  
        self.checksword = checksword
        self.mode = mode
    def move(self):   
        self.hitboxes = (self.posx,self.posy+20,32,10)  
        #pygame.draw.rect(self.screen,(0,0,0),self.hitboxes,1)
        if self.direction == 1:
            self.posx += 40 
        if self.direction == -1: 
            self.posx -= 40  
    def draw(self):  
        if (self.mode == False and self.checksword == False)or(self.mode == True and self.checksword == True) :
            if self.direction == -1:
                self.screen.blit(self.bulletimg_left, (self.posx,self.posy)) 
            if self.direction == 1:
                self.screen.blit(self.bulletimg_right, (self.posx,self.posy))
    def off_screen(self): 
        return not (self.posx>= 0 and self.posx <= self.screen_width) 
