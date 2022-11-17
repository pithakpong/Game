import pygame  
import random
class Boss(pygame.sprite.Sprite): 
    def __init__(self):  
        super().__init__()
        self.x = random.randint(300,700) 
        self.y = random.randint(300,400)  
        self.shoot = "not ready"
        self.turn = "right idle"  
        self.bossimg = [] 
        self.beamimg = [] 
        # idle right
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_rightidle_1.png"),(300,300)))
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_rightidle_2.png"),(300,300))) 
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_rightidle_3.png"),(300,300)))
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_rightidle_4.png"),(300,300)))

        # idle left
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_leftidle_1.png"),(300,300)))
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_leftidle_2.png"),(300,300))) 
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_leftidle_3.png"),(300,300)))
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_leftidle_4.png"),(300,300)))
        
        # attack right
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackright_1.png"),(300,300)))
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackright_2.png"),(300,300))) 
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackright_3.png"),(300,300)))
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackright_4.png"),(300,300)))
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackright_5.png"),(300,300))) 
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackright_6.png"),(300,300)))
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackright_7.png"),(300,300))) 

        #attack left 
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackleft_1.png"),(300,300)))
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackleft_2.png"),(300,300))) 
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackleft_3.png"),(300,300)))
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackleft_4.png"),(300,300)))
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackleft_5.png"),(300,300))) 
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackleft_6.png"),(300,300)))
        self.bossimg.append(pygame.transform.scale(pygame.image.load("images/boss_attackleft_7.png"),(300,300)))  

        # ----------------------------------   beam  ----------------------------- # 
        
        # beam right
        self.beamimg.append(pygame.transform.scale(pygame.image.load("images/beamright_1.png"),(1000,25))) 
        self.beamimg.append(pygame.transform.scale(pygame.image.load("images/beamright_2.png"),(1000,25))) 
        self.beamimg.append(pygame.transform.scale(pygame.image.load("images/beamright_3.png"),(1000,25)))

        #beam left  
        self.beamimg.append(pygame.transform.scale(pygame.image.load("images/beamleft_1.png"),(1000,25)))
        self.beamimg.append(pygame.transform.scale(pygame.image.load("images/beamleft_2.png"),(1000,25)))
        self.beamimg.append(pygame.transform.scale(pygame.image.load("images/beamleft_3.png"),(1000,25)))
        

        # frame animation boss 
        
        self.currentframe_boss = 0  
        self.image = self.bossimg[self.currentframe_boss]   

        self.rect = self.image.get_rect() 
        self.rect.topleft = [self.x,self.y]
        # frame animation beam   
        
        self.currentframe_beam = 0 
        self.frame_beam = self.beamimg[self.currentframe_beam]

        #hitboxes 
        self.hitboxes = (self.x + 30,self.y,260,280)
        


    def move(self,xtrack,ytrack,surface): 
        #update position
        self.rect.topleft = [self.x,self.y]  
        #update hitboxes 
        self.hitboxes = (self.x + 30,self.y,260,280)
        #pygame.draw.rect(surface,(0,0,0),pygame.Rect(self.hitboxes),1)
        if (self.y - ytrack > 10 or self.y - ytrack < -10):
            if self.y < ytrack: 
                self.y += 2
            if self.y > ytrack: 
                self.y -= 2 
            self.shoot = "not ready" 
        else : 
            self.shoot = "ready"
        if self.x < xtrack - 150: 
            self.turn = "right idle" 
        if self.x > xtrack - 150:  
            self.turn = "left idle"
    def attack(self,surface,bossState):  
        if  self.shoot == "not ready":
            self.currentframe_beam = 0
        if self.shoot == "ready" and bossState == "appear": 
            self.currentframe_beam += 0.1 
            if self.currentframe_beam >=4 : 
                self.currentframe_beam = 0
            if self.turn == "right idle" and self.shoot == "ready":  
                self.frame_beam = self.beamimg[int(self.currentframe_beam)]
                surface.blit(self.frame_beam,(self.x+200,self.y + 80))
            if self.turn == "left idle" and self.shoot == "ready":
                self.frame_beam = self.beamimg[int(self.currentframe_beam) + 2]
                surface.blit(self.frame_beam,(self.x-900,self.y + 80))

    def update(self):
        self.currentframe_boss += 0.1 
        if self.turn == "right idle" and self.shoot == "not ready": 
            if self.currentframe_boss >= 4 : 
                self.currentframe_boss = 0 
            self.image = self.bossimg[int(self.currentframe_boss)]
        if self.turn == "left idle" and self.shoot == "not ready":  
            if self.currentframe_boss + 4 >= 8: 
                self.currentframe_boss = 0
            self.image = self.bossimg[int(self.currentframe_boss) + 4] 
        if self.turn == "right idle" and self.shoot == "ready":
            if self.currentframe_boss + 8 >= 15: 
                self.currentframe_boss = 0 
            self.image = self.bossimg[int(self.currentframe_boss) + 8] 
        if self.turn == "left idle" and self.shoot == "ready": 
            if self.currentframe_boss + 16 >= 22: 
                self.currentframe_boss = 0 
            self.image = self.bossimg[int(self.currentframe_boss) + 16]