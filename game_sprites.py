import pygame as py
from settings import *
vec = py.math.Vector2

class Player(py.sprite.Sprite):
    def __init__(self,platforms):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((30,30))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2,HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.platforms = platforms

    def update(self):
        keystat = py.key.get_pressed()
        if keystat[py.K_RIGHT]:
            self.acc.x = player_acc
        if keystat[py.K_LEFT]:
            self.acc.x = - player_acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.acc.x += self.vel.x * player_fric
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc
        self.rect.midbottom = self.pos
        self.acc = vec(0,0.5)

    def jump(self):
        hits = py.sprite.spritecollide(self,self.platforms,False)
        if hits:
            self.vel.y = -player_jump

class Platforms(py.sprite.Sprite):
    def __init__(self,w,h,x,y):
        py.sprite.Sprite.__init__(self)
        self.image = py.Surface((w,h))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self):
        pass