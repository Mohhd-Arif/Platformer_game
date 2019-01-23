import pygame as py
from settings import *
import random
from game_sprites import Player,Platforms
running = True

class Main_game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode((WIDTH,HEIGHT))
        py.display.set_caption("hello world")
        self.clock = py.time.Clock()
        self.playing = True
        self.mysprites()

    def mysprites(self):
        self.all_sprites = py.sprite.Group()

        self.platforms = py.sprite.Group()#---------adding platforms---------
        p1 = Platforms(WIDTH,20,WIDTH/2,HEIGHT - 30)
        self.add_platform(p1)
        p2 = Platforms(70,20,WIDTH/2, HEIGHT - 100)
        self.add_platform(p2)
        for plat in platforms_list:
            px = Platforms(*plat)
            self.add_platform(px)

        self.player = Player(self.platforms)#----------------adding player--------
        self.all_sprites.add(self.player)

    def add_platform(self,x):
        self.platforms.add(x)
        self.all_sprites.add(x)

    def player_movement(self):
        if self.player.vel.y > 0:
            hits = py.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
                self.player.acc.y = 0

        if self.player.rect.top < HEIGHT/3:
            self.player.pos.y += abs(self.player.vel.y)

            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top > HEIGHT:
                    plat.kill()

        if self.player.rect.top > HEIGHT-50:
            for plat in self.platforms:
                plat.rect.y -= max(self.player.vel.y, 10)
                if plat.rect.bottom < 0:
                    plat.kill()

            if len(self.platforms) == 0:
                self.playing = False

    def platform_manage(self):
        while len(self.platforms) < 5:
            width = random.randrange(50,95)
            px = Platforms(width,20,
                           random.randrange(0+width -30,WIDTH-width+30),
                           random.randrange(-70,-30))

            self.add_platform(px)


    def main_loop(self):
        while self.playing:
            for e in py.event.get():
                if e.type == py.QUIT:
                    self.playing = False
                    global running
                    running = False
                if e.type == py.KEYDOWN:
                    if e.key == py.K_SPACE:
                        self.player.jump()

            self.player_movement()
            self.platform_manage()

            self.all_sprites.update()

            self.screen.fill(white)
            self.all_sprites.draw(self.screen)
            py.display.flip()
            self.clock.tick(fps)

        py.quit()

while running:
    play = Main_game()
    play.main_loop()