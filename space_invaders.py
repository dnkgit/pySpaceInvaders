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
