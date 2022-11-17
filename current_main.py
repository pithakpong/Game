
import pygame  
import button 
import image
import player 
import background_state
import Enemies  
import bullet
import random
from bomb import Bomb 
from bomb import BombShow  
from potion import Potion
from boss import Boss
from sword import Sword
from inputText import Text_input
from sound import song 
from sound import SoundEffect

pygame.init()  
clock = pygame.time.Clock()
screen_width = 1000 
screen_height = 700 
TITLE = "Game Project" 
screen = pygame.display.set_mode((screen_width, screen_height))  
pygame.display.set_caption(TITLE)
# initial object 
objimg = image.Images() 
backgroungobj = background_state.Background()
#objbut = button.Button()


# initial image 
start_img = objimg.start_img
exit_img = objimg.exit_img 
background_img = objimg.background_img 
gameover_img = objimg.gameover_img 
replay_img = objimg.replay_img 
quit_img = objimg.quit_img 
bomb_img = objimg.bombimg 
bomb_effect = objimg.bombeffect
win_img = objimg.win
score_img = objimg.score_img
gameover_img = pygame.transform.scale(gameover_img,(1000,700))
background_img = pygame.transform.scale(background_img,(1000,700)) 

# initial button 
start_button = button.Button(399,317,start_img,1)
exit_button = button.Button(400,500,exit_img,1)
replay_button = button.Button(50,500,replay_img,0.3)
quit_button = button.Button(750,500,quit_img,1)
score_button = button.Button(420,400,score_img,0.5)

# initial player 
player = player.Player(screen_width/2,screen_height/2,screen_width,screen_height,0.001,screen)
#initial enemies
enemies_move = pygame.sprite.Group()  
enemies = []  
remove = False
for enemy in range(5):
    enemy = Enemies.Enemy()  
    enemies.append(enemy) 
    enemies_move.add(enemy) 
#initial bullet  
bulletstore = []
#initial bomb
statebomb = False
bomblist = [] 
bombshow = []
Bombgo = False
bombcount = 0
keepBomb = False

#initial potion 
potionshow = []
keepPotion = False 

#initial sword 
swordShow = [] 
keepsword = False

#initial boss
Boss_move = pygame.sprite.Group() 
boss = Boss() 
bosslist = [boss] 
Boss_move.add(boss)
#slash 
slash = False
menuState = "main"
moveing_sprites = pygame.sprite.Group() 
moveing_sprites.add(player)
i = 0 
direct = 1 
enemycount = 5 
# initial text boxes input 
player_name = ''
input_rect = pygame.Rect(500,200,140,32) 
base_font = pygame.font.Font(None,32)
color_active = pygame.Color('gray100') 
color_passive = pygame.Color('gray0') 
color = color_passive 
active = False  
#initial score  
score = 0
def writeText(Text,color,posx,posy): 
    font = pygame.font.Font(None,32)
    this_surface = font.render(Text,True,color) 
    pygame.draw.rect(screen,(0,255,0),(posx,posy,170,32))
    screen.blit(this_surface,(posx,posy))

# -------------------------------------------------------------- work with file ----------------------------------------------------- #
#open mode read
sctxt = open("scorebar.txt", 'r') 
pltxt = open("playername.txt", 'r')  
#input
scin = sctxt.read() 
plin = pltxt.read()

#handle input 

    #score 
scorex = "" 
scorelist = []
scindex = -1 
    #player name 
playerx = "" 
playerlist = [] 
plindex = -1

 # -------------------- input ---------------------- # 
 # handle input score
for x in scin: 
    scindex += 1 
    scorex += x 
    if x == '\n' or scindex == len(scin)-1: 
        scorelist.append(scorex)
        scorex = ""  
# handle input player name
for x in plin: 
    plindex += 1 
    playerx += x 
    if x == '\n' or plindex == len(plin)-1: 
        playerlist.append(playerx)
        playerx = ""
toggle = True 
# ---------- player name ----------------- #
playername_first = Text_input(screen,"1. "+playerlist[0],(0,0,0),20,200,1)
playername_second = Text_input(screen,"2. "+playerlist[1],(0,0,0),20,250,1)
playername_third = Text_input(screen,"3. "+playerlist[2],(0,0,0),20,300,1) 
playername_fourth = Text_input(screen,"4. "+playerlist[3],(0,0,0),20,350,1)
playername_fifth = Text_input(screen,"5. "+playerlist[4],(0,0,0),20,400,1) 

# ------------ score list ---------------- # 
score_first = Text_input(screen,scorelist[0],(0,0,0),300,200,1)
score_second = Text_input(screen,scorelist[1],(0,0,0),300,250,1)
score_third = Text_input(screen,scorelist[2],(0,0,0),300,300,1)
score_fourth = Text_input(screen,scorelist[3],(0,0,0),300,350,1)
score_fifth = Text_input(screen,scorelist[4],(0,0,0),300,400,1) 

# -------------- Title ------------------- # 
Title_text = Text_input(screen,"Score Bar\n",(0,0,0),280,100,3)

#---------------- Current score ------------------3  
Text_current_score_end = Text_input(screen,"SCORE : \n",(255,255,0),300,500,2)
Text_current_score = Text_input(screen,"SCORE : \n",(0,0,0),650,30,1)
#inital song and sound
menuSong = song(1,90) 
winSong = song(2,90)  
# ---- sound effect ------- #
effect_slash = SoundEffect(1) 
effect_playerhurt = SoundEffect(2) 
effect_health = SoundEffect(3) 
effect_gameover = SoundEffect(4) 
effect_bomb = SoundEffect(5)  
effect_enemy_sound = SoundEffect(6)
effect_enemy_hurt = SoundEffect(7)
effect_gun = SoundEffect(8) 
effect_beam = SoundEffect(9) 
effect_bosshurt = SoundEffect(10) 
effect_bossdead = SoundEffect(11)
running = True 
while running : 
    print(backgroungobj.bossHealth,backgroungobj.bossappear)
    timemillis = pygame.time.get_ticks()
    #initail bomb
    bomb_player = Bomb(screen,player.x,player.y,player.check_idle)
    #initail bullet 
    if direct == 1:
        bullet_player = bullet.Bullet(player.x+50,player.y+10,direct,screen,screen_width,player.toggle,player.checksword) 
    if direct == -1:  
        bullet_player = bullet.Bullet(player.x-20,player.y+10,direct,screen,screen_width,player.toggle,player.checksword) 
    #print(player.check_idle,player.playerState)
    #print(enemy.attackState + " " + str(enemy.current_sprite_enemy))
    if menuState == "main" : 
        menuSong.play()
        screen.blit(background_img,(i,0))  
        screen.blit(background_img,(1000+i,0))   



    # move background image
        if i == -1000: 
            screen.blit(background_img,(1000+i,0)) 
            i = 0

        i-=1
        if start_button.draw(screen) and menuState == "main":
            menuSong.stop() 
            menuState = "playing"
        if exit_button.draw(screen)  and menuState == "main": 
            running = False 
        if score_button.draw(screen) and menuState == "main":  
            menuState = "score"
        #text input  
        writeText("Key your name: ",(0,0,0),300,200)
        pygame.draw.rect(screen,color,input_rect,2)
        text_surface = base_font.render(player_name,True,(0,255,0))
        screen.blit(text_surface,(input_rect.x +5,input_rect.y+5)) 
        input_rect.w = max(text_surface.get_width()+10,100)  
        # check state text input 
        if active == True : 
            color = color_active 
        else : 
            color = color_passive   

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        # click on text boxes
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos): 
                active = True 
            else : 
                active = False
        
        if event.type == pygame.KEYDOWN:  
            # key name
            if active == True and menuState == "main": 
                if event.key == pygame.K_BACKSPACE: 
                    player_name = player_name[:-1] 
                else : 
                    player_name += event.unicode
            if event.key == pygame.K_d:  
                if menuState == "playing": 
                    player.right_pressed = True
                    player.playerState = "move right"
                    player.check_idle = "right idle" 
                    direct = 1  
            if event.key == pygame.K_a:  
                if menuState == "playing":
                    player.left_pressed = True
                    player.playerState = "move left"  
                    player.check_idle = "left idle"
                    direct = -1  
            if event.key == pygame.K_w:   
                if menuState == "playing":
                    player.up_pressed = True 
            if event.key == pygame.K_s: 
                if menuState == "playing": 
                    player.down_pressed = True 
            if event.key == pygame.K_SPACE:  
                if menuState == "playing":
                    player.shoot = "shoot"
                    bulletstore.append(bullet_player)  
                    slash = True
                    if (bullet_player.mode == False and bullet_player.checksword == False)or(bullet_player.mode == True and bullet_player.checksword == True):
                        effect_gun.play()
                    else: 
                        effect_slash.play()
                    
            if event.key == pygame.K_i:  
                if menuState == "playing":
                    keepBomb = True
                    keepPotion = True
                    keepsword = True
            if event.key == pygame.K_o: 
                if menuState == "playing":
                    Bombgo = True  
            if event.key == pygame.K_k:  
                if player.checksword == True and menuState == "playing":
                    player.toggle = not player.toggle 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                if menuState == "playing":
                    player.playerState = "idle" 
                    player.right_pressed = False
            if event.key == pygame.K_a: 
                if menuState == "playing":
                    player.playerState = "idle"
                    player.left_pressed = False 
            if event.key == pygame.K_w:
                if menuState == "playing":
                    player.playerState = "idle"  
                    player.up_pressed = False 
            if event.key == pygame.K_s: 
                if menuState == "playing":
                    player.playerState = "idle" 
                    player.down_pressed = False
            if event.key == pygame.K_i:
                if menuState == "playing": 
                    keepBomb = False 
                    keepPotion = False
                    keepsword = False
            if event.key == pygame.K_o: 
                if menuState == "playing":
                    Bombgo = False 
            if event.key == pygame.K_k: 
                pass 
            if event.key == pygame.K_SPACE: 
                if menuState == "playing":
                    slash = False 

   
    if menuState == "playing":   
        score_current = Text_input(screen,str(score)+'\n',(0,0,0),800,30,1)
        backgroungobj.draw(screen)
        Text_current_score.draw()
        score_current.draw()
        player.update()  
        moveing_sprites.draw(screen) 
        moveing_sprites.update()
        for enemy in enemies : 
            enemy.move(player.x,player.y,screen) 
            #effect_enemy_sound.play() 
        # bullet update
        for bullet_player in bulletstore: 
            bullet_player.draw()
            bullet_player.move()
            if bullet_player.off_screen == True: 
                bulletstore.remove(bullet_player) 
        #collision  shoot 
        for enemy in enemies: 
            #remove = False
            for bullet_player in bulletstore:
                if (bullet_player.mode == False and bullet_player.checksword == False)or(bullet_player.mode == True and bullet_player.checksword == True):
                    if ((enemy.hitboxes[0] < bullet_player.hitboxes[0] < enemy.hitboxes[0] + enemy.hitboxes[2] or enemy.hitboxes[0] < bullet_player.hitboxes[0] + bullet_player.hitboxes[2] < enemy.hitboxes[0] + enemy.hitboxes[2])and (enemy.hitboxes[1] < bullet_player.hitboxes[1] < enemy.hitboxes[1] + enemy.hitboxes[3] or enemy.hitboxes[1] < bullet_player.hitboxes[1] + bullet_player.hitboxes[3] < enemy.hitboxes[1] + enemy.hitboxes[3])):
                        #initial sword
                        #remove = True
                        if enemy.y <= 244: 
                            sword = Sword(enemy.x,280,screen)
                        else: 
                            sword = Sword(enemy.x,enemy.y,screen)
                        bulletstore.remove(bullet_player)     
                        #if remove :  
                        if enemy in enemies:
                            enemies.remove(enemy) 
                            enemies_move.remove(enemy)
                            effect_enemy_hurt.play()
                            score += 100  
                        #drop Bomb
                        if  random.randint(0,9) == 1: 
                            if enemy.y <= 244:
                                bombshow.append(BombShow(enemy.x,280,screen))
                            else : 
                                bombshow.append(BombShow(enemy.x, enemy.y,screen)) 
                        #drop Potion
                        if random.randint(0,4) == 3: 
                            if enemy.y <= 244: 
                                potionshow.append(Potion(enemy.x,280,screen))
                            else :
                                potionshow.append(Potion(enemy.x, enemy.y,screen))  
                        if player.checksword == False: 
                            #drop sword
                            if  random.randint(0,14) == 5 and sword.getsword == False:
                                swordShow.append(sword)
                else: 
                    if ((enemy.hitboxes[0] < player.hitboxes[0] < enemy.hitboxes[0] + enemy.hitboxes[2] or enemy.hitboxes[0] <player.hitboxes[0] + player.hitboxes[2] < enemy.hitboxes[0] + enemy.hitboxes[2])and (enemy.hitboxes[1] < player.hitboxes[1] < enemy.hitboxes[1] + enemy.hitboxes[3] or enemy.hitboxes[1] <player.hitboxes[1] + player.hitboxes[3] < enemy.hitboxes[1] + enemy.hitboxes[3])  and slash == True):
                        #initial sword
                        if enemy.y <= 244:
                            sword = Sword(enemy.x,280,screen)
                        else:
                            sword = Sword(enemy.x,enemy.y,screen)
                        enemies.remove(enemy) 
                        enemies_move.remove(enemy)
                        effect_enemy_hurt.play()
                        score += 100 
                        slash = False
                        bulletstore.remove(bullet_player)  
                        #drop Bomb
                        if  random.randint(0,9) == 1:
                            if enemy.y <= 244: 
                                bombshow.append(BombShow(enemy.x,280,screen))
                            else : 
                                bombshow.append(BombShow(enemy.x, enemy.y,screen)) 
                        #drop Potion
                        if random.randint(0,4) == 3:  
                            if enemy.y <= 244: 
                                potionshow.append(Potion(enemy.x,280,screen))
                            else:
                                potionshow.append(Potion(enemy.x, enemy.y,screen))  
                        if player.checksword == False: 
                            #drop sword
                            if  random.randint(0,14) == 5 and sword.getsword == False: 
                                swordShow.append(sword)
                     
                    
                    


        #spawn enemy
        if len(enemies) == 0:  
            enemycount += 1 
            for enemy in range(enemycount): 
                enemy = Enemies.Enemy()  
                enemies.append(enemy) 
                enemies_move.add(enemy)
        #boss appear
        if len(enemies) == 10: 
            backgroungobj.bossappear = "appear"  
        # BOSS
        if backgroungobj.bossappear == "appear" :
            boss.attack(screen,backgroungobj.bossappear)
            Boss_move.draw(screen) 
            Boss_move.update()
            boss.move(player.x,player.y-80,screen) 
            for bullet_player in bulletstore:  
                if (bullet_player.mode == False and bullet_player.checksword == False)or(bullet_player.mode == True and bullet_player.checksword == True):
                    if ((boss.hitboxes[0] < bullet_player.hitboxes[0] < boss.hitboxes[0] + boss.hitboxes[2] or boss.hitboxes[0] < bullet_player.hitboxes[0] + bullet_player.hitboxes[2] < boss.hitboxes[0] + boss.hitboxes[2])and (boss.hitboxes[1] < bullet_player.hitboxes[1] < boss.hitboxes[1] + boss.hitboxes[3] or boss.hitboxes[1] < bullet_player.hitboxes[1] + bullet_player.hitboxes[3] < boss.hitboxes[1] + boss.hitboxes[3])):
                        bulletstore.remove(bullet_player) 
                        backgroungobj.bossHealth -= 1
                        effect_bosshurt.play()
                else: 
                    if ((boss.hitboxes[0] < player.hitboxes[0] < boss.hitboxes[0] + boss.hitboxes[2] or boss.hitboxes[0] <player.hitboxes[0] + player.hitboxes[2] < boss.hitboxes[0] + boss.hitboxes[2])and (boss.hitboxes[1] < player.hitboxes[1] < boss.hitboxes[1] + boss.hitboxes[3] or boss.hitboxes[1] <player.hitboxes[1] + player.hitboxes[3] < boss.hitboxes[1] + boss.hitboxes[3])and slash == True):
                        backgroungobj.bossHealth -= 5
                        effect_bosshurt.play()
                        slash = False

            if int(boss.currentframe_beam) == 3: 
                effect_beam.play() 
                backgroungobj.playerHealth -= 3 
                effect_playerhurt.play() 
                boss.currentframe_beam = 0 
            if boss.currentframe_beam > 0 : 
                player.playerState = "hurt"
                effect_beam.play() 
            if backgroungobj.bossHealth <= 0 :
                effect_bossdead.play()   
                for boss in bosslist:
                    bosslist.remove(boss)  
                    Boss_move.remove(boss)
                    score += 5000 
                backgroungobj.bossappear = "not appear"
                menuState = "win"
        if backgroungobj.bossHealth <= 0 :   
            backgroungobj.bossHealth = 0 
        
        # update player health bar
        for enemy in enemies : 
            if enemy.attackState == "attack" and enemy.current_sprite_enemy == 0: 
                backgroungobj.playerHealth -= 1
                effect_playerhurt.play() 
                player.playerState = "hurt" 

        if backgroungobj.playerHealth <= 0 : 
            menuState = "gameover"


        enemies_move.draw(screen)
        enemies_move.update() 
        #bomb Go 
        if bombcount > 0 and Bombgo == True : 
            bomblist.append(Bomb(screen,player.x,player.y,player.check_idle))  
            bombcount -= 1
            Bombgo = False
        #display ball
        for bomb in bomblist : 
            if bomb.draw(): 
                bomblist.remove(bomb)  
                bomb.draweffect()
                effect_bomb.play()
                for enemy in enemies : 
                    if ((bomb.hitboxes[0] < enemy.hitboxes[0] < bomb.hitboxes[0]+bomb.hitboxes[2]) or (bomb.hitboxes[0] < enemy.hitboxes[0] + enemy.hitboxes[2] < bomb.hitboxes[0]+bomb.hitboxes[2])) and ((bomb.hitboxes[1] < enemy.hitboxes[1] < bomb.hitboxes[1]+bomb.hitboxes[3]) or (bomb.hitboxes[1] < enemy.hitboxes[1] + enemy.hitboxes[3] < bomb.hitboxes[1]+bomb.hitboxes[3])):
                        #initial sword 
                        if enemy.y <= 244 : 
                            sword = Sword(enemy.x,280,screen)
                        else:
                            sword = Sword(enemy.x, enemy.y,screen)
                        enemies.remove(enemy) 
                        enemies_move.remove(enemy)
                        score += 100 
                        #drop Bomb
                        if  random.randint(0,9) == 1:
                            if enemy.y <= 244: 
                                bombshow.append(BombShow(enemy.x,280,screen))
                            else:
                                bombshow.append(BombShow(enemy.x, enemy.y,screen)) 
                        #drop Potion
                        if random.randint(0,4) == 3:  
                            if enemy.y <= 244: 
                                potionshow.append(Potion(enemy.x,280,screen))
                            else:
                                potionshow.append(Potion(enemy.x, enemy.y,screen)) 
                        #drop sword
                        if player.checksword == False:
                            if  random.randint(0,14) == 5 and sword.getsword == False:
                                swordShow.append(sword) 
                if ((bomb.hitboxes[0] < boss.hitboxes[0] < bomb.hitboxes[0]+bomb.hitboxes[2]) or (bomb.hitboxes[0] < boss.hitboxes[0] + boss.hitboxes[2] < bomb.hitboxes[0]+bomb.hitboxes[2])) and ((bomb.hitboxes[1] < boss.hitboxes[1] < bomb.hitboxes[1]+bomb.hitboxes[3]) or (bomb.hitboxes[1] < boss.hitboxes[1] + boss.hitboxes[3] < bomb.hitboxes[1]+bomb.hitboxes[3])) and backgroungobj.bossappear =="appear":
                    effect_bosshurt.play()
                    backgroungobj.bossHealth -= 10
        
        #bomb show drop
        for bombimg in bombshow: 
            bombimg.draw() 
            if keepBomb == True and (( player.hitboxes[0] < bombimg.hitboxes[0] < player.hitboxes[0]+ player.hitboxes[2] or player.hitboxes[0] < bombimg.hitboxes[0] + bombimg.hitboxes[2]< player.hitboxes[0]+ player.hitboxes[2]) and (player.hitboxes[1] < bombimg.hitboxes[1] < player.hitboxes[1]+ player.hitboxes[3] or player.hitboxes[1] < bombimg.hitboxes[1] + bombimg.hitboxes[3] < player.hitboxes[1]+ player.hitboxes[3])):
                bombcount += 1
                bombshow.remove(bombimg)
        #potion show drop 
        for potion in potionshow: 
            potion.draw() 
            if keepPotion == True and (( player.hitboxes[0] < potion.hitboxes[0] < player.hitboxes[0]+ player.hitboxes[2] or player.hitboxes[0] < potion.hitboxes[0] + potion.hitboxes[2]< player.hitboxes[0]+ player.hitboxes[2]) and (player.hitboxes[1] < potion.hitboxes[1] < player.hitboxes[1]+ player.hitboxes[3] or player.hitboxes[1] < potion.hitboxes[1] + potion.hitboxes[3] < player.hitboxes[1]+ player.hitboxes[3])):
                effect_health.play()
                if backgroungobj.playerHealth <= 9:
                    backgroungobj.playerHealth += 1
                potionshow.remove(potion) 
        #sword show drop 
        for sword in swordShow: 
            sword.draw() 
            if keepsword == True and (( player.hitboxes[0] < sword.hitboxes[0] < player.hitboxes[0]+ player.hitboxes[2] or player.hitboxes[0] < sword.hitboxes[0] + sword.hitboxes[2]< player.hitboxes[0]+ player.hitboxes[2]) and (player.hitboxes[1] < sword.hitboxes[1] < player.hitboxes[1]+ player.hitboxes[3] or player.hitboxes[1] < sword.hitboxes[1] + sword.hitboxes[3] < player.hitboxes[1]+ player.hitboxes[3])):
                swordShow.remove(sword)
                player.checksword = True
        
    #game over
    if menuState == "gameover" :    
        score_current_win = Text_input(screen,str(score)+'\n',(0,0,0),500,500,2)
        Text_current_score_win = Text_input(screen,"SCORE : \n",(0,0,0),300,500,2)
        effect_gameover.play()
         #change background 
        screen.blit(gameover_img,(0,0))  
        score_current_win.draw()
        Text_current_score_win.draw() 
        # reset enemy
        if quit_button.draw(screen)  and menuState == "gameover": 
                # -------------------- process ----------------------- #  
            #toggle = True
            for x in range(len(scorelist)): 
                if score >= int(scorelist[x]) and toggle == True: 
                    # change score
                    scorelist.insert(x,str(score)+'\n') 
                    scorelist.pop(len(scorelist)-1) 
                    # change player name 
                    playerlist.insert(x,player_name+'\n') 
                    playerlist.pop(len(playerlist)-1)
                    toggle = False 

            running = False
    
    if menuState == "win": 
        score_current_end = Text_input(screen,str(score)+'\n',(0,0,0),500,500,2)
        winSong.play()
        screen.fill((255,255,255))
        screen.blit(win_img,(250,100))
        Text_current_score_end.draw()
        score_current_end.draw()
        if quit_button.draw(screen)  and menuState == "win": 
                # -------------------- process ----------------------- #  
            #toggle = True
            for x in range(len(scorelist)): 
                if score >= int(scorelist[x]) and toggle == True: 
                    # change score 
                    scorelist.insert(x,str(score)+'\n') 
                    scorelist.pop(len(scorelist)-1) 
                    # change player name 
                    playerlist.insert(x,player_name+'\n') 
                    playerlist.pop(len(playerlist)-1)

                    toggle = False 
            running = False
    if menuState == "score": 
        screen.fill((0,255,0))
        # draw name
        playername_first.draw()
        playername_second.draw() 
        playername_third.draw() 
        playername_fourth.draw() 
        playername_fifth.draw() 
        # draw score
        score_first.draw() 
        score_second.draw() 
        score_third.draw()  
        score_fourth.draw()  
        score_fifth.draw() 
        # draw Title 
        Title_text.draw() 
        if quit_button.draw(screen) and menuState == "score": 
            menuState = "main"
    pygame.display.update()
    clock.tick(30)
# ----------------------- send data -------------------- #  
# value sent 
plsend = "" 
scsend = "" 
for i in playerlist:
    plsend += i 
for i in scorelist: 
    scsend += i
#print(plsend)  
#print(scsend) 
sctxt = open("scorebar.txt",'w') 
pltxt = open("playername.txt",'w')
sctxt.write(scsend)
pltxt.write(plsend)
sctxt.close() 
pltxt.close() 

pygame.quit() 