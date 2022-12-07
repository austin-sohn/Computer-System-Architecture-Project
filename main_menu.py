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
  listofGames = ["Pong", "Space Invaders" "Not Super Mario"]
  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
          index += 1
          if index > len(listofGames):
            index = 2
        elif event.key == pygame.K_s:
          index -= 1
          if index < 0:
            index = 0
        elif event.key == pygame.K_o:
          print(listofGames[index])
          break

    screen.fill(BLACK)
    text = menuFont.render('quit' , True , WHITE)
    screen.blit(text , (0,0))
    pygame.display.update() 

if __name__ == "__main__":
  main()