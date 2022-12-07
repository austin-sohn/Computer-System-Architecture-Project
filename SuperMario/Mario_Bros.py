from SuperMario.data import main as mmain
from SuperMario.data import menu as menu
from SuperMario.data import config as c
import pygame as pg
import os
import sys

class App():
    def __init__(self):
        self.menu = None
        self.main = None

    def run(self):
        self.menu = menu.Menu() 
        self.menu.menu_loop()
        if self.menu.quit_state == 'play': #Check whether to continue to game or quit app
            self.main = mmain.Main()
            self.main.main_loop()
            if self.main.quit_state == 'menu':
                os.execl(sys.executable, sys.executable, *sys.argv) #Restart game

def main():
    pg.init() #Initialize pygame module
    c.screen = pg.display.set_mode((c.SCREEN_SIZE.x, c.SCREEN_SIZE.y))
    pg.display.set_caption(c.CAPTION)
    c.clock = pg.time.Clock()

    app = App()
    app.run()

    pg.quit()
if __name__ == '__main__':
    main()