import sys, pygame, os

DEFAULT_PLAYER_SIZE = (10,50) # width, height
DEFAULT_BALL_SIZE = (50,50) # width, height
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
    if key[pygame.K_w] and direction== "v": # up key
      self.y -= p_speed # move up
    elif key[pygame.K_s] and direction == "v": # down key
      self.y += p_speed # move down
    if key[pygame.K_o] and direction == "h": # left key
      self.y -= p_speed # move up
    elif key[pygame.K_l] and direction == "h": # right key
      self.y += p_speed # move down

  def draw(self, surface): # xy[0] == x, xy[1] == y
    surface.blit(self.player, (self.x, self.y))

class Ball(object):
  def __init__(self):
    image_ball = pygame.image.load("./images/white_circle.png")
    self.ball = pygame.transform.scale(image_ball, DEFAULT_BALL_SIZE)
    self.x = width/2
    self.y = height/2
  def draw(self, surface):
    surface.blit(self.ball, (self.x, self.y))

def fps_counter(clock, window):
  font = pygame.font.SysFont("Arial" , 18 , bold = True)
  fps = str(int(clock.get_fps()))
  fps_t = font.render(fps , 1, pygame.Color("RED"))
  window.blit(fps_t,(width/2,height-50))
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
  # ballrect = ball.get_rect()
  # p1rect = p1.get_rect()
  # p2rect = p1.get_rect()
 
  clock = pygame.time.Clock()
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
      if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_q: # exits game if you press q
          sys.exit()
        elif event.key == pygame.K_SPACE or event.key == pygame.K_r: # resets game if you press space or r
          screen.fill(black)
          
    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #   speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #   speed[1] = -speed[1]
    p1.handle_keys("v")
    p2.handle_keys("h")
    screen.fill(black)
   
    p1.draw(screen)
    p2.draw(screen)
    fps_counter(clock, screen) 
    #print(clock.get_fps())
    # b.draw(screen)
    pygame.display.update() # update the screen
    clock.tick(30)
    #pygame.display.flip()

if __name__ == "__main__":
  main()