from random import random
import pyxel

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2

STAR_COUNT = 100
STAR_COLOUR_HIGH = 12
STAR_COLOUR_LOW = 5

PLAYER_WIDTH = 8
PLAYER_HEIGHT = 8
PLAYER_SPEED = 2

BULLET_WIDTH = 2
BULLET_HEIGHT = 8
BULLET_COLOUR = 11
BULLET_SPEED = 4

ENEMY_WIDTH = 8
ENEMY_HEIGHT = 8
ENEMY_SPEED = 1.5

BLAST_START_RADIUS = 1
BLAST_END_RADIUS = 8
BLAST_COLOUR_IN = 7
BLAST_COLOUR_OUT = 10

enemy_list = []
bullet_list = []
blast_list = []

def update_list(list):
    for elem in list:
        elem.update()

def draw_list(list):
    for elem in list:
        elem.draw()

def cleanup_list(list):
    i = 0
    while i < len(list):
        elem = list[i]
        if not elem.alive:
            list.pop(i)
        else:
            i = i + 1

class Background:
    def __init__(self):
        self.star_list = []
        for i in range(STAR_COUNT):
            self.star_list.append(random() * pyxel.width, random() * pyxel.height, random() * 1.5 + 1)

    def update(self):
        for i,(x,y,speed) in enumerate(self.star_list):
            y += speed
            if y > pyxel.height:
                y = pyxel.height
            self.star_list[i] = (x,y,speed)

    def draw(self):
        for (x,y,speed) in self.star_list:
            pyxel.pset(x,y,STAR_COLOUR_HIGH if speed > 1.8 else STAR_COLOUR_LOW)

class Player:
    def __init__(self):
        self.x = x
        self.y = y
        self.w = PLAYER_WIDTH
        self.h = PLAYER_HEIGHT
        self.alive = True

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= PLAYER_SPEED

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += PLAYER_SPEED

        if pyxel.btn(pyxel.KEY_UP):
            self.y += PLAYER_SPEED

        if pyxel.btn(pyxel.KEY_DOWN):
            self.y -= PLAYER_SPEED

        self.x = max(self.x, 0)
        self.x = min(self.x, pyxel.width - self.w)

        self.y = max(self.y, 0)
        self.y = min(self.y, pyxel.height - self.w)

        if pyxel.btn(pyxel.KEY_SPACE):
            Bullet(self.x + (PLAYER_WIDTH - BULLET_WIDTH) / 2, self.y + BULLET_HEIGHT / 2)

        pyxel.play(0,0)

        def draw(self):
            pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h, 0)

class Bullet:
    def __init__(self, x, y)
        self.x = x
        self.y = y
        self.w = BULLET_WIDTH
        self.h = BULLET_HEIGHT
        self.alive = True

        bullet_list.append(self)

    def update(self):
        self.y -= BULLET_SPEED

        if self.y + self.h - 1 < 0:
            self.alive = False

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, BULLET_COLOUR)

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = ENEMY_WIDTH
        self.h = ENEMY_HEIGHT
        self.dir = 1
        self.alive = True
        self.offset = int(random() * 60)

        enemy_list.append(self)

    def update(self):
        if(pyxel.frame_count + self.offset) % 60 < 30:
            self.x += ENEMY_SPEED
            self.dir = 1
        else:
            self.y -= ENEMY_SPEED
            self.dir = -1
        self.y += ENEMY_SPEED

        if self.y > pyxel.height -1:
            self.alive = False
        
    def draw(self):
        pyxel.blit(self.x, self.y, 0, 8, 0, self.w * self.dir, self.h, 0)
        
class Blast:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = BLAST_START_RADIUS
        self.alive = True
        blast_list.append(self)

    def update(self):
        self.radius += 1

        if self.radius > BLAST_END_RADIUS:
            self.alive = False

    def draw(self):
        pyxel.circ(self.x, self.y, self.radius, BLAST_COLOUR_IN)
        pyxel.circb(self.x, self.y, self.radius, BLAST_COLOUR_OUT)

class App:

    def __init__(self):
        pyxel.init(120, 160, caption="Dan Space Invaders")

        pyxel.image(0).set(
            0,
            0,
            [
                "00c00c00",
                "0c7007c0",
                "0c7007c0",
                "c703b007c",
                "77033077",
                "785cc587",
                "85c77c58",
                "0c0880c0"
            ]
        )

        pyxel.image(0).set(
            8,
            0,
            [
                "00088000",
                "00ee1200",
                "08e2b180",
                "02882820",
                "00222200",
                "00012280",
                "08208008",
                "80008000"
            ]
        )

        pyxel.sound(0).set("a3a2c1a1", "p", "7", "s", 5)
        pyxel.sound(1).set("a3a2c2c2", "n", "7742", "s", 10)

        set.scene = SCENE_TITLE
        self.score = 0
        self.background = Background()
        self.player = Player(pyxel.width/2, pyxel.height - 20)
        pyxel.run(self.update, self.draw)

