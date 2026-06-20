import pygame
from pygame.locals import*
import random

pygame.init()
clock=pygame.time.Clock()
fps=60

screen_width=864
screen_height=936

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("flappy bird")

#game variables

font=pygame.font.Sysfont("Times new roman", 60)
white=(255,255,255)
ground_scroll=0
scroll_speed=4
flying=False
game_over=False
PipeGap=150
PipeFrenquency=1500  #milliseconds
Last_Pipe=pygame.time.get_ticks()
score=0
Pass_Pipe=False

#load images

bg=pygame.image.load("BG.png")
ground_img=pygame.image.load("Ground.png")
re_button=pygame.image.load("Restart.png")

#function for placing text ont he screen

def draw_text(text, font, text_col, x, y):
    img=font.render(text, True, text_col)
    screen.blit(img,( x, y))
    

def reset():
    Pipe_group.empty()
    
    


class Bird(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite. __init__ (self)
        self.images=[]
        self.index=0
        self.counter=0
        
        for i in range(1,3):
            image=pygame.image.load(f"bird{i}.png")
            self.images.append(image)

        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.vel=0
        self.clicked=False()

    def update(self):
        if flying == True:
            # appling gravity
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y = self.rect.y + int(self.vel)

        if game_over == False:
            # Jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked==False:
                self.clicked = True
                self.vel = -10

            if pygame.mouse.get.pressed()[0] == 0: 
                self.clicked=False

            flap_cooldown=5
            self.counter+=1

            if self.counter > flap_cooldown:
                self.counter=0 
                self.index=self.index+1   
                if self.index >= len(self.images):
                    self.index=0

                self.image=self.images[self.index]
            self.image=pygame.transform.rotate(self.images[self.index], self.vel * -2)
            
        else:
            self.image=pygame.transform.rotate(self.images[self.index], -90)
