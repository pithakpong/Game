import pygame 
from pygame import mixer 
class song: 
    def __init__(self,number,volume): 
        self.volume = float(volume/100)
        self.number = number 
        self.toggle = True
    def play(self): 
        if self.number == 1: 
            if self.toggle == True: 
                mixer.music.load("sound/Dumb_ways_to_die.mp3") 
                mixer.music.set_volume(self.volume) 
                mixer.music.play(-1) 
                self.toggle = False

        if self.number == 2: 
            if self.toggle == True: 
                mixer.music.load("sound/winsound.mp3") 
                mixer.music.set_volume(self.volume)
                mixer.music.play(-1)
                self.toggle = False
    def stop(self): 
        mixer.music.stop()
class SoundEffect: 
    def __init__(self,number): 
        self.number = number 
        self.slash = pygame.mixer.Sound("sound/slash.wav") 
        self.player_hurt = pygame.mixer.Sound("sound/player_hurt.wav")  
        self.healthsound = pygame.mixer.Sound("sound/healthsound.wav")  
        self.gameover = pygame.mixer.Sound("sound/gameover_effect.wav")
        self.bombsound = pygame.mixer.Sound("sound/bombsound.wav")
        self.enemy_sound = pygame.mixer.Sound("sound/enemy_sound.wav") 
        self.enemy_hurtsound = pygame.mixer.Sound("sound/enemy_hurtsound.wav") 
        self.gun_sound = pygame.mixer.Sound("sound/gun_sound.wav") 
        self.beam = pygame.mixer.Sound("sound/beam.wav") 
        self.boss_hurt = pygame.mixer.Sound("sound/boss_hurt.wav") 
        self.boss_dead = pygame.mixer.Sound("sound/boss_dead.wav")
        
    def play(self):
        if self.number == 1: 
            self.slash.play() 
        if self.number == 2:
            self.player_hurt.play() 
        if self.number == 3: 
            self.healthsound.play() 
        if self.number == 4: 
            self.gameover.play() 
        if self.number == 5:  
            self.bombsound.play() 
        if self.number == 6:  
            self.enemy_sound.play() 
        if self.number == 7: 
            self.enemy_hurtsound.play() 
        if self.number == 8:  
            self.gun_sound.play()
        if self.number == 9: 
            self.beam.play() 
        if self.number == 10:  
            self.boss_hurt.play() 
        if self.number == 11:  
            self.boss_dead.play()