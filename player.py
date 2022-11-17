import pygame 
class Player(pygame.sprite.Sprite): 
    def __init__(self,x,y,w_x,w_y,scale,surface): 
        #self.rect = pygame.Rect(x,y,32,32)  
        self.surface = surface
        self.fullscreen = pygame.Rect(0,0,w_x,w_y)
        self.x = int(x) 
        self.y = int(y)  
        self.w_x = int(w_x)  
        self.w_y = int(w_y)
        self.scale = scale  
        self.color = (250,120,60)  
        self.bg_color = (55,55,55) 
        self.velX = 0 
        self.velY = 0 
        self.right_pressed = False 
        self.left_pressed = False 
        self.up_pressed = False 
        self.down_pressed = False 
        self.checksword = False 
        self.toggle = False
        super().__init__() 
        self.sprites = []  
        # right move
        self.sprites.append(pygame.image.load('images/player_move_right_1.png'))
        self.sprites.append(pygame.image.load('images/player_move_right_2.png'))
        self.sprites.append(pygame.image.load('images/player_move_right_3.png'))
        self.sprites.append(pygame.image.load('images/player_move_right_4.png'))
        self.sprites.append(pygame.image.load('images/player_move_right_5.png'))

        # left move
        self.sprites.append(pygame.image.load('images/player_move_left_1.png'))
        self.sprites.append(pygame.image.load('images/player_move_left_2.png'))
        self.sprites.append(pygame.image.load('images/player_move_left_3.png'))
        self.sprites.append(pygame.image.load('images/player_move_left_4.png'))
        self.sprites.append(pygame.image.load('images/player_move_left_5.png')) 

        # left idle 
        self.sprites.append(pygame.image.load('images/player_idle_left_1.png'))
        self.sprites.append(pygame.image.load('images/player_idle_left_2.png'))
        self.sprites.append(pygame.image.load('images/player_idle_left_3.png'))
        self.sprites.append(pygame.image.load('images/player_idle_left_4.png')) 

        #right idle 
        self.sprites.append(pygame.image.load('images/player_idle_right_1.png'))
        self.sprites.append(pygame.image.load('images/player_idle_right_2.png'))
        self.sprites.append(pygame.image.load('images/player_idle_right_3.png'))
        self.sprites.append(pygame.image.load('images/player_idle_right_4.png')) 

        #shoot left 
        self.sprites.append(pygame.image.load('images/player_shootleft_1.png'))
        self.sprites.append(pygame.image.load('images/player_shootleft_2.png'))
        self.sprites.append(pygame.image.load('images/player_shootleft_3.png'))
        self.sprites.append(pygame.image.load('images/player_shootleft_4.png'))

        #shoot right
        self.sprites.append(pygame.image.load('images/player_shootright_1.png'))
        self.sprites.append(pygame.image.load('images/player_shootright_2.png'))
        self.sprites.append(pygame.image.load('images/player_shootright_3.png'))
        self.sprites.append(pygame.image.load('images/player_shootright_4.png'))

        #hurt left 
        self.sprites.append(pygame.image.load('images/playerhurtleft_1.png'))
        self.sprites.append(pygame.image.load('images/playerhurtleft_2.png'))
        self.sprites.append(pygame.image.load('images/playerhurtleft_3.png'))
        self.sprites.append(pygame.image.load('images/playerhurtleft_4.png')) 

        #hurt right 
        self.sprites.append(pygame.image.load('images/playerhurtright_1.png'))
        self.sprites.append(pygame.image.load('images/playerhurtright_2.png'))
        self.sprites.append(pygame.image.load('images/playerhurtright_3.png'))
        self.sprites.append(pygame.image.load('images/playerhurtright_4.png'))

    # ------------------------------- sword man upload  ------------------------------ #

        # right move
        self.sprites.append(pygame.image.load('images/swordman_turnright_1.png')) 
        self.sprites.append(pygame.image.load('images/swordman_turnright_2.png'))
        self.sprites.append(pygame.image.load('images/swordman_turnright_3.png'))
        self.sprites.append(pygame.image.load('images/swordman_turnright_4.png'))
        self.sprites.append(pygame.image.load('images/swordman_turnright_5.png'))
        self.sprites.append(pygame.image.load('images/swordman_turnright_6.png'))
        self.sprites.append(pygame.image.load('images/swordman_turnright_7.png')) 

        # left move 
        self.sprites.append(pygame.image.load('images/swordman_turnleft_1.png')) 
        self.sprites.append(pygame.image.load('images/swordman_turnleft_2.png')) 
        self.sprites.append(pygame.image.load('images/swordman_turnleft_3.png')) 
        self.sprites.append(pygame.image.load('images/swordman_turnleft_4.png')) 
        self.sprites.append(pygame.image.load('images/swordman_turnleft_5.png')) 
        self.sprites.append(pygame.image.load('images/swordman_turnleft_6.png')) 
        self.sprites.append(pygame.image.load('images/swordman_turnleft_7.png'))  

        # idle left 
        self.sprites.append(pygame.image.load('images/swordman_idleleft_1.png')) 
        self.sprites.append(pygame.image.load('images/swordman_idleleft_2.png')) 
        self.sprites.append(pygame.image.load('images/swordman_idleleft_3.png')) 
        self.sprites.append(pygame.image.load('images/swordman_idleleft_4.png'))  

        # idle right 
        self.sprites.append(pygame.image.load('images/swordman_idleright_1.png')) 
        self.sprites.append(pygame.image.load('images/swordman_idleright_2.png')) 
        self.sprites.append(pygame.image.load('images/swordman_idleright_3.png')) 
        self.sprites.append(pygame.image.load('images/swordman_idleright_4.png'))  

        # slash left 
        self.sprites.append(pygame.image.load('images/swordman_attackleft_1.png'))
        self.sprites.append(pygame.image.load('images/swordman_attackleft_2.png'))
        self.sprites.append(pygame.image.load('images/swordman_attackleft_3.png'))
        self.sprites.append(pygame.image.load('images/swordman_attackleft_4.png'))
        self.sprites.append(pygame.image.load('images/swordman_attackleft_5.png'))
        self.sprites.append(pygame.image.load('images/swordman_attackleft_6.png')) 
        
        # slash right
        self.sprites.append(pygame.image.load('images/swordman_attackright_1.png'))
        self.sprites.append(pygame.image.load('images/swordman_attackright_2.png'))
        self.sprites.append(pygame.image.load('images/swordman_attackright_3.png'))
        self.sprites.append(pygame.image.load('images/swordman_attackright_4.png'))
        self.sprites.append(pygame.image.load('images/swordman_attackright_5.png'))
        self.sprites.append(pygame.image.load('images/swordman_attackright_6.png')) 

        # idle right
        self.sprites.append(pygame.image.load('images/swordman_idleright_1.png')) 
        self.sprites.append(pygame.image.load('images/swordman_idleright_2.png')) 
        self.sprites.append(pygame.image.load('images/swordman_idleright_3.png')) 
        self.sprites.append(pygame.image.load('images/swordman_idleright_4.png')) 


        #transform move left 
        self.sprites[5] = pygame.transform.scale(self.sprites[5],(70,100))
        self.sprites[6] = pygame.transform.scale(self.sprites[6],(70,100))
        self.sprites[7] = pygame.transform.scale(self.sprites[7],(70,100))
        self.sprites[8] = pygame.transform.scale(self.sprites[8],(70,100))
        self.sprites[9] = pygame.transform.scale(self.sprites[9],(70,100))


        # transform move right
        self.sprites[0] = pygame.transform.scale(self.sprites[0],(70,100))
        self.sprites[1] = pygame.transform.scale(self.sprites[1],(70,100))
        self.sprites[2] = pygame.transform.scale(self.sprites[2],(70,100))
        self.sprites[3] = pygame.transform.scale(self.sprites[3],(70,100))
        self.sprites[4] = pygame.transform.scale(self.sprites[4],(70,100))

        # transform idle left
        self.sprites[10] = pygame.transform.scale(self.sprites[10],(70,100))
        self.sprites[11] = pygame.transform.scale(self.sprites[11],(70,100))
        self.sprites[12] = pygame.transform.scale(self.sprites[12],(70,100))
        self.sprites[13] = pygame.transform.scale(self.sprites[13],(70,100))

        # transform idle right
        self.sprites[14] = pygame.transform.scale(self.sprites[14],(70,100))
        self.sprites[15] = pygame.transform.scale(self.sprites[15],(70,100))
        self.sprites[16] = pygame.transform.scale(self.sprites[16],(70,100))
        self.sprites[17] = pygame.transform.scale(self.sprites[17],(70,100))

        # transform shoot left
        self.sprites[18] = pygame.transform.scale(self.sprites[18],(70,100))
        self.sprites[19] = pygame.transform.scale(self.sprites[19],(70,100))
        self.sprites[20] = pygame.transform.scale(self.sprites[20],(70,100))
        self.sprites[21] = pygame.transform.scale(self.sprites[21],(70,100)) 

        # transform shoot right
        self.sprites[22] = pygame.transform.scale(self.sprites[22],(70,100))
        self.sprites[23] = pygame.transform.scale(self.sprites[23],(70,100))
        self.sprites[24] = pygame.transform.scale(self.sprites[24],(70,100))
        self.sprites[25] = pygame.transform.scale(self.sprites[25],(70,100))  

        # transform hurt left 
        self.sprites[26] = pygame.transform.scale(self.sprites[26],(70,100))
        self.sprites[27] = pygame.transform.scale(self.sprites[27],(70,100))
        self.sprites[28] = pygame.transform.scale(self.sprites[28],(70,100))
        self.sprites[29] = pygame.transform.scale(self.sprites[29],(70,100))  

        # transform hurt right
        self.sprites[30] = pygame.transform.scale(self.sprites[30],(70,100))
        self.sprites[31] = pygame.transform.scale(self.sprites[31],(70,100))
        self.sprites[32] = pygame.transform.scale(self.sprites[32],(70,100))
        self.sprites[33] = pygame.transform.scale(self.sprites[33],(70,100))   

    # --------------------------------------- sword man transform ------------------------------- #
        # transform move right
        self.sprites[34] = pygame.transform.scale(self.sprites[34],(70,100))
        self.sprites[35] = pygame.transform.scale(self.sprites[35],(70,100))
        self.sprites[36] = pygame.transform.scale(self.sprites[36],(70,100))
        self.sprites[37] = pygame.transform.scale(self.sprites[37],(70,100))
        self.sprites[38] = pygame.transform.scale(self.sprites[38],(70,100))
        self.sprites[39] = pygame.transform.scale(self.sprites[39],(70,100))
        self.sprites[40] = pygame.transform.scale(self.sprites[40],(70,100))

        # transform move left
        self.sprites[41] = pygame.transform.scale(self.sprites[41],(70,100))
        self.sprites[42] = pygame.transform.scale(self.sprites[42],(70,100))
        self.sprites[43] = pygame.transform.scale(self.sprites[43],(70,100))
        self.sprites[44] = pygame.transform.scale(self.sprites[44],(70,100))
        self.sprites[45] = pygame.transform.scale(self.sprites[45],(70,100))
        self.sprites[46] = pygame.transform.scale(self.sprites[46],(70,100))
        self.sprites[47] = pygame.transform.scale(self.sprites[47],(70,100))

        # transform idle left
        self.sprites[48] = pygame.transform.scale(self.sprites[48],(70,100))
        self.sprites[49] = pygame.transform.scale(self.sprites[49],(70,100))
        self.sprites[50] = pygame.transform.scale(self.sprites[50],(70,100))
        self.sprites[51] = pygame.transform.scale(self.sprites[51],(70,100))

        # transform idle right
        self.sprites[52] = pygame.transform.scale(self.sprites[42],(70,100))
        self.sprites[53] = pygame.transform.scale(self.sprites[43],(70,100))
        self.sprites[54] = pygame.transform.scale(self.sprites[54],(70,100))
        self.sprites[55] = pygame.transform.scale(self.sprites[55],(70,100))

        # transform left slash 
        self.sprites[56] = pygame.transform.scale(self.sprites[56],(70,100))
        self.sprites[57] = pygame.transform.scale(self.sprites[57],(70,100))
        self.sprites[58] = pygame.transform.scale(self.sprites[58],(70,100))
        self.sprites[59] = pygame.transform.scale(self.sprites[59],(70,100))
        self.sprites[60] = pygame.transform.scale(self.sprites[60],(70,100))
        self.sprites[61] = pygame.transform.scale(self.sprites[61],(70,100)) 

        # transform right slash 
        self.sprites[62] = pygame.transform.scale(self.sprites[62],(70,100))
        self.sprites[63] = pygame.transform.scale(self.sprites[63],(70,100))
        self.sprites[64] = pygame.transform.scale(self.sprites[64],(70,100))
        self.sprites[65] = pygame.transform.scale(self.sprites[65],(70,100))
        self.sprites[66] = pygame.transform.scale(self.sprites[66],(70,100))
        self.sprites[67] = pygame.transform.scale(self.sprites[67],(70,100)) 

        # transform idle right
        self.sprites[68] = pygame.transform.scale(self.sprites[68],(70,100))
        self.sprites[69] = pygame.transform.scale(self.sprites[69],(70,100))
        self.sprites[70] = pygame.transform.scale(self.sprites[70],(70,100))
        self.sprites[71] = pygame.transform.scale(self.sprites[71],(70,100))


        self.current_sprite = 0 
        self.image = self.sprites[self.current_sprite]

        # get size
        self.rect = pygame.Rect(0,0,50,50)
        #self.width = self.image.get_width() 
        #self.height = self.image.get_height()  

        #self.rect = pygame.transform.scale(self.image,(int(self.width * self.scale),int(self.height * self.scale)))
        
        self.image.set_colorkey((0,0,0)) 
        self.rect.topleft = [self.x,self.y] 
        self.hitboxes = (self.x,self.y,70,100)
        self.speed = 6
        self.playerState = "idle" 
        self.check_idle =  "right idle"
        self.shoot = "not shoot"

        
    def draw_screen(self,surface): 
        pygame.draw.rect(surface,self.bg_color,self.fullscreen)

    def draw(self,surface): 
        pygame.draw.rect(surface,self.color,self.rect)
    
    def update(self): 
        self.current_sprite += 0.2

        #check animation  
        if self.checksword == False or self.toggle == True: 
            if self.playerState == "move right":
                if self.current_sprite >= 5:
                    self.current_sprite = 0 
                self.image = self.sprites[int(self.current_sprite)]
            if self.playerState == "move left": 
                if self.current_sprite + 5 >= 10: 
                    self.current_sprite = 0 
                self.image = self.sprites[int(self.current_sprite)+5] 
            if self.playerState == "idle" and self.check_idle == "left idle":
                if self.current_sprite + 9 >= 14: 
                    self.current_sprite = 0 
                self.image = self.sprites[int(self.current_sprite)+9] 
            if self.playerState == "idle" and self.check_idle == "right idle": 
                if self.current_sprite + 13 >= 18: 
                    self.current_sprite = 1 
                self.image = self.sprites[int(self.current_sprite)+13]
            if self.shoot == "shoot" and self.check_idle == "left idle":
                if self.current_sprite + 18 >= 22: 
                    self.current_sprite = 0 
                    self.shoot = "not shoot"
                self.image = self.sprites[int(self.current_sprite)+18]
            if self.shoot == "shoot" and self.check_idle == "right idle":
                if self.current_sprite + 21 >= 25: 
                    self.current_sprite = 1
                    self.shoot = "not shoot" 
                self.image = self.sprites[int(self.current_sprite)+22] 
            
            if self.playerState == "hurt" and self.check_idle == "left idle":
                if self.current_sprite + 26 >= 30: 
                    self.current_sprite = 0
                    self.playerState = "not hurt" 
                self.image = self.sprites[int(self.current_sprite)+26]

            if self.playerState == "hurt" and self.check_idle == "right idle":
                if self.current_sprite + 30 >= 34: 
                    self.current_sprite = 0
                    self.playerState = "not hurt" 
                self.image = self.sprites[int(self.current_sprite)+30]
        
        if self.checksword == True and not(self.toggle == True) : 
            if self.playerState == "move right" and self.shoot == "not shoot":
                if self.current_sprite + 34 >= 40:
                    self.current_sprite = 0  
                    self.shoot ="not shoot"
                self.image = self.sprites[int(self.current_sprite) + 34]
            if self.playerState == "move left" and self.shoot == "not shoot" :  
                if self.current_sprite + 41 >= 47: 
                    self.current_sprite = 0 
                    self.shoot == "not shoot"
                self.image = self.sprites[int(self.current_sprite)+41] 
            if self.playerState == "idle" and self.check_idle == "left idle" and self.shoot == "not shoot": 
                if self.current_sprite + 48 >= 51: 
                    self.current_sprite = 0
                    self.shoot ="not shoot" 
                self.image = self.sprites[int(self.current_sprite)+48] 
            if self.playerState == "idle" and self.check_idle == "right idle" and self.shoot == "not shoot" : 
                if self.current_sprite + 69 >= 71: 
                    self.current_sprite = 0
                    self.shoot ="not shoot"
                self.image = self.sprites[int(self.current_sprite)+69]
            if self.shoot == "shoot" and self.check_idle == "left idle": 
                if self.current_sprite + 56 >= 61: 
                    self.current_sprite = 0 
                    self.shoot = "not shoot"
                self.image = self.sprites[int(self.current_sprite)+56]
            if self.shoot == "shoot" and self.check_idle == "right idle":
                if self.current_sprite + 62 >= 67: 
                    self.current_sprite = 0
                    self.shoot = "not shoot" 
                self.image = self.sprites[int(self.current_sprite)+62] 


        
        self.velX = 0 
        self.velY = 0 
        if self.x >=0 and self.y >=0 and self.x <= 1000 and self.y <= 700:
            if self.left_pressed and not self.right_pressed: 
                self.velX = -self.speed  
            if self.right_pressed and not self.left_pressed: 
                self.velX = self.speed 
            if self.up_pressed and not self.down_pressed: 
                self.velY = -self.speed 
            if self.down_pressed and not self.up_pressed:  
                self.velY = self.speed  
        
        if self.x <= 0 : 
            self.x =0 
        if self.x >= 930: 
            self.x = 930 
        if self.y <=250: 
            self.y =250
        if self.y >= 600: 
            self.y = 600 
            

        self.x += self.velX 
        self.y += self.velY
        self.hitboxes = (self.x,self.y,60,100)
        #pygame.draw.rect(self.surface,(0,0,0),self.hitboxes,1) 
        self.rect.topleft = [self.x,self.y]
        #print(self.x,self.y)

        #self.rect = pygame.Rect(self.x, self.y,32,32)
