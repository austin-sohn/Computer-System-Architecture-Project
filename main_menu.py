import pygame, sys

WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)

def main():
  pygame.init()
  menuFont = pygame.font.SysFont('Corbel',35)
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("Main Menu")
  index = 0
  listofGames = ["Pong", "Space Invaders", "Not Super Mario", "Quit"]
  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
          index += 1
          if index > len(listofGames):
            index = len(listofGames)-1
        elif event.key == pygame.K_w:
          index -= 1
          if index < 0:
            index = 0
        elif event.key == pygame.K_o:
          if index == len(listofGames)-1: # if position is last, quit
            sys.exit()
          elif index == 0: # first position is pong
            print("go to pong")
          elif index == 1: # second position is space invaders
            print("go to Space Invaders")
          elif index == 2: # third position is mario
            print("go to Not Super Mario")
          break
      
    screen.fill(BLACK)
    fourth = 0
    for game in listofGames:
      text = menuFont.render(game, True , WHITE)
      text_rect = text.get_rect(center=(WIDTH/2, fourth+75))
      screen.blit(text , text_rect)
      fourth += HEIGHT/4
    pygame.display.update() 

if __name__ == "__main__":
  main()