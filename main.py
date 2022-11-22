import sys, pygame, os

DEFAULT_PLAYER_SIZE = (10,50) # width, height
DEFAULT_BALL_SIZE = (15,15) # width, height
size = width, height = 800, 600


class Players(object):
  def __init__(self, spawn):
    self.image_rectangle = pygame.image.load("./images/white_rectangle.jpg")
    self.player = pygame.transform.scale(self.image_rectangle, DEFAULT_PLAYER_SIZE)
    self.rect = self.player.get_rect()
    self.x = spawn[0]
    self.y = spawn[1]

  def handle_keys(self, direction):
    # Handles Keys
    key = pygame.key.get_pressed()
    p_speed = 6
    if key[pygame.K_w] and direction== 1: # up key
      self.y -= p_speed # move up
    elif key[pygame.K_s] and direction == 1: # down key
      self.y += p_speed # move down
    if key[pygame.K_o] and direction == 2: # left key
      self.y -= p_speed # move up
    elif key[pygame.K_l] and direction == 2: # right key
      self.y += p_speed # move down

  def draw_player(self, surface): # xy[0] == x, xy[1] == y
    surface.blit(self.player, (self.x, self.y))

class Ball(object):
  def __init__(self):
    image_ball = pygame.image.load("./images/white_circle.png")
    self.ball = pygame.transform.scale(image_ball, DEFAULT_BALL_SIZE)
    self.x = width/2
    self.y = height/2

  def draw_ball(self, surface):
    surface.blit(self.ball, (self.x, self.y))

class HUD(object):
  def __init__(self):
    self.font = pygame.font.SysFont("Arial" , 18 , bold = True)
    self.p1_score = 0
    self.p2_score = 0

  def score_point(self, p):
    if p == 1:
      self.p1_score += 1
    elif p == 2:
      self.p2_score += 1

  def fps_counter(self, clock, window):
    fps = str(int(clock.get_fps()))
    fps_t = self.font.render(fps , 1, pygame.Color("RED"))
    window.blit(fps_t,(width/2,height-50))

  def draw_score(self, window):
    middle = width/2
    p1Score_t = self.font.render(str(self.p1_score), 1, (255,255,255))
    p2Score_t = self.font.render(str(self.p2_score), 1, (255,255,255))
    window.blit(p1Score_t, (middle - (middle/2), 10))
    window.blit(p2Score_t, (middle + (middle/2), 10))

def main():
  pygame.init()
  
  speed = [1, 1]
  black = 0, 0, 0

  screen = pygame.display.set_mode(size)
  p1Spawn = [10,10]
  p2Spawn=[width-10-DEFAULT_PLAYER_SIZE[0], 10]
  p1 = Players(p1Spawn)
  p2 = Players(p2Spawn)
  b = Ball()
  hud = HUD()
 
  clock = pygame.time.Clock()
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
      if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_q: # exits game if you press q
          sys.exit()
        elif event.key == pygame.K_SPACE or event.key == pygame.K_r: # resets game if you press space or r
          screen.fill(black)
          
   
    p1.handle_keys(1)
    p2.handle_keys(2)
    screen.fill(black)
   
    p1.draw_player(screen)
    p2.draw_player(screen)

    b.draw_ball(screen)
    hud.draw_score(screen)
    # if ballrect.left < 0 or ballrect.right > width:
    #   speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #   speed[1] = -speed[1]

    hud.fps_counter(clock, screen) 

    pygame.display.update() # update the screen
    clock.tick(30)

if __name__ == "__main__":
  main()