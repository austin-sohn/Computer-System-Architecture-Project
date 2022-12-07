import sys
import pygame as pg
from SpaceInvaders.vector import Vector as Vector
from SpaceInvaders.laser import Laser as Laser

LEFT, RIGHT, UP, DOWN, STOP = 'left', 'right', 'up', 'down', 'stop'

dirs = {LEFT: Vector(-1, 0),
        RIGHT: Vector(1, 0),
        UP: Vector(0, -1),
        DOWN: Vector(0, 1),
        STOP: Vector(0, 0)}

dir_keys = {pg.K_LEFT: LEFT, pg.K_w: LEFT,
            pg.K_RIGHT: RIGHT, pg.K_s: RIGHT,
            pg.K_UP: UP,
            pg.K_DOWN: DOWN}

def check_events(game):
    ship = game.ship

    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit()
        elif e.type == pg.KEYDOWN:
            if e.key in dir_keys:
                v = dirs[dir_keys[e.key]]
                ship.inc_add(v)
            elif e.key == pg.K_SPACE or e.key == pg.K_o:
              game.ship.toggle_firing()
        elif e.type == pg.KEYUP:
            if e.key in dir_keys:
                v = dirs[dir_keys[e.key]]
                ship.inc_add(-v)
            elif e.key == pg.K_SPACE or e.key == pg.K_o:
              game.ship.toggle_firing()

