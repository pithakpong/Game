import pygame 
import random 
class Enemy(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__() 
        self.x = random.randint(60,400)
        self.y = random.randint(60,400)
        #self.rect = pygame.Rect(self.x,self.y,20,20) 
        self.sprites_enemies = [] 
        self.enemyState = 'idle' 
        self.checkenemy = 'idle'  

        #right run
        self.sprites_enemies.append(pygame.image.load('images/ghost_runright_1.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_runright_2.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_runright_3.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_runright_4.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_runright_5.png'))  
        self.sprites_enemies.append(pygame.image.load('images/ghost_runright_6.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_runright_7.png'))

        #left run
        self.sprites_enemies.append(pygame.image.load('images/ghost_runleft_1.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_runleft_2.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_runleft_3.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_runleft_4.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_runleft_5.png')) 
        self.sprites_enemies.append(pygame.image.load('images/ghost_runleft_6.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_runleft_7.png'))  

        #left idle 
        self.sprites_enemies.append(pygame.image.load('images/ghost_idleleft_1.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_idleleft_2.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_idleleft_3.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_idleleft_4.png')) 

        #right idle
        self.sprites_enemies.append(pygame.image.load('images/ghost_idleright_1.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_idleright_2.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_idleright_3.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_idleright_4.png')) 

        #dead left
        self.sprites_enemies.append(pygame.image.load('images/ghost_deadleft_1.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_deadleft_2.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_deadleft_3.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_deadleft_4.png'))

        #dead right 
        self.sprites_enemies.append(pygame.image.load('images/ghost_deadright_1.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_deadright_2.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_deadright_3.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_deadright_4.png'))  


        #attack right 
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackright_1.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackright_2.png')) 
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackright_3.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackright_4.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackright_5.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackright_6.png')) 
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackright_7.png')) 


        #attack left
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackleft_1.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackleft_2.png')) 
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackleft_3.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackleft_4.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackleft_5.png'))
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackleft_6.png')) 
        self.sprites_enemies.append(pygame.image.load('images/ghost_attackleft_7.png'))





        self.hitboxes = (self.x,self.y,100,80)  
        #enemy dead
        self.deadframe = 0 
        self.frame = self.sprites_enemies[self.deadframe]

        self.current_sprite_enemy = 0 
        self.image = self.sprites_enemies[self.current_sprite_enemy]

        self.rect = pygame.Rect(0,0,50,50) 
        self.image.set_colorkey((0,0,0)) 
        self.rect.center = [self.x,self.y]
        self.attackState = "no attack"

    def move(self,targetx,targety,surface):  
        if self.x - targetx > 4 or self.x -targetx <-4: 
            
            if self.x < targetx: 
                self.enemyState ="right run" 
                self.checkenemy = "right idle"
                self.attackState = "no attack"
                self.x += 5
            if self.x > targetx:
                self.enemyState ="left run"
                self.checkenemy = "left idle" 
                self.attackState = "no attack"
                self.x -= 5  
        else: 
            if self.y > targety:  
                self.y -= 5
                self.attackState = "no attack" 
            if self.y < targety: 
                self.y += 5
                self.attackState = "no attack"  
            if self.y - targety <= 4 and self.y -targety >= -4 : 
                self.enemyState ="idle" 
                self.attackState = "attack" 
        #self.attackState = False
        self.hitboxes = (self.x,self.y-20,70,100) 
        #pygame.draw.rect(screen,(0,0,0),self.hitboxes,1)
        self.rect.center = [self.x,self.y]

    def draw(self): 
        #pygame.draw.rect(win,(0,0,0),pygame.Rect(self.x,self.y,20,20)) 
        pass

    def attack(self):  
        pass

    def update(self):  
        self.current_sprite_enemy += 0.2 
        if self.enemyState == "right run": 
            if self.current_sprite_enemy >= 7: 
                self.current_sprite_enemy = 0 
            self.image = self.sprites_enemies[int(self.current_sprite_enemy)] 
        if self.enemyState == "left run": 
            if self.current_sprite_enemy + 7 >= 14: 
                self.current_sprite_enemy = 0 
            self.image = self.sprites_enemies[int(self.current_sprite_enemy) + 7]
        if self.enemyState == "idle" and self.checkenemy == "left idle": 
            if self.current_sprite_enemy + 11 >= 18: 
                self.current_sprite_enemy = 0 
            self.image = self.sprites_enemies[int(self.current_sprite_enemy) + 11] 
        if self.enemyState == "idle" and self.checkenemy == "right idle":  
            if self.current_sprite_enemy + 15 >= 22: 
                self.current_sprite_enemy = 0 
            self.image = self.sprites_enemies[int(self.current_sprite_enemy) + 15] 
        if self.attackState == "attack"and self.checkenemy == "right idle": 
            if self.current_sprite_enemy + 30 >= 38: 
                self.current_sprite_enemy = 0  
            self.image = self.sprites_enemies[int(self.current_sprite_enemy) + 30]
        if self.attackState == "attack" and self.checkenemy == "left idle": 
            if self.current_sprite_enemy + 37 >= 45: 
                self.current_sprite_enemy = 0
            self.image = self.sprites_enemies[int(self.current_sprite_enemy) + 37]
