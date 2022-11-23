import sys, pygame, random

DEFAULT_PLAYER_SIZE = (10,50) # width, height
DEFAULT_BALL_SIZE = (15,15) # width, height
SIZE = WIDTH, HEIGHT = 800, 600
INITIAL_SCORE = [0, 0]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Players(object):
  def __init__(self, spawn):
    self.image_rectangle = pygame.image.load("./images/white_rectangle.jpg")
    self.player = pygame.transform.scale(self.image_rectangle, DEFAULT_PLAYER_SIZE)
    self.x = spawn[0]
    self.y = spawn[1]
    self.rect_player = pygame.Rect(self.x,self.y,10,50)
    self.player_vel = 8

  def handle_keys(self, direction):
    # Handles Keys
    key = pygame.key.get_pressed()
    print(self.rect_player.y)
    if self.rect_player.y <= 0:
      self.rect_player.y = 0 
    elif self.rect_player.y >= HEIGHT-DEFAULT_PLAYER_SIZE[1]:
      self.rect_player.y = HEIGHT-DEFAULT_PLAYER_SIZE[1]
    if key[pygame.K_w] and direction== 1: # up key
      self.rect_player.y -= self.player_vel
    elif key[pygame.K_s] and direction == 1: # down key
      self.rect_player.y += self.player_vel
    if key[pygame.K_o] and direction == 2: # left key
      self.rect_player.y -= self.player_vel
    elif key[pygame.K_l] and direction == 2: # right key
      self.rect_player.y += self.player_vel

  def draw_player(self, surface):
   pygame.draw.rect(surface, WHITE, self.rect_player); 

class Ball(object):
  def __init__(self):
    image_ball = pygame.image.load("./images/white_circle.png")
    self.ball = pygame.transform.scale(image_ball, DEFAULT_BALL_SIZE)
    self.x = WIDTH/2
    self.y = HEIGHT/2
    self.rect_ball = pygame.Rect(self.x,self.y,15,15)

  def draw_ball(self, surface):
    pygame.draw.ellipse(surface, WHITE, self.rect_ball); 

  def move_ball(self, ball_vel):
    self.x += ball_vel[0]
    self.y += ball_vel[1]
    self.rect_ball.topleft = (self.x, self.y)
    if self.rect_ball.top < 0 or self.rect_ball.bottom > HEIGHT:
      ball_vel[1] = -ball_vel[1]

class HUD(object):
  def __init__(self, hud_score):
    self.font = pygame.font.SysFont("Arial" , 18 , bold = True)
    self.p1_score = hud_score[0]
    self.p2_score = hud_score[1]
    
  def score_point(self, p):
    if p == 1:
      self.p1_score += 1
    elif p == 2:
      self.p2_score += 1

  def fps_counter(self, clock, window):
    fps = str(int(clock.get_fps()))
    fps_t = self.font.render(fps , 1, pygame.Color("RED"))
    window.blit(fps_t,(WIDTH/2,HEIGHT-50))

  def draw_score(self, window):
    middle = WIDTH/2
    p1Score_t = self.font.render(str(self.p1_score), 1, WHITE)
    p2Score_t = self.font.render(str(self.p2_score), 1, WHITE)
    window.blit(p1Score_t, (middle - (middle/2), 10))
    window.blit(p2Score_t, (middle + (middle/2), 10))

def main():
  pygame.init()
  screen = pygame.display.set_mode(SIZE)
  clock = pygame.time.Clock()
  p1Spawn = [10,10]
  p2Spawn=[WIDTH-10-DEFAULT_PLAYER_SIZE[0], 10]
  p1 = Players(p1Spawn)
  p2 = Players(p2Spawn)
  b = Ball()
  hud = HUD(INITIAL_SCORE)
  ball_speed = 10
  ball_start_x = random.choice((-ball_speed, ball_speed))
  ball_start_y = random.choice((-ball_speed, ball_speed))
  ball_vel = [ball_start_x, ball_start_y]
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
      if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_q: # exits game if you press q
          sys.exit()
        elif event.key == pygame.K_SPACE or event.key == pygame.K_r: # resets game if you press space or r
          p1 = Players(p1Spawn)
          p2 = Players(p2Spawn)
          b = Ball()
          hud = HUD(INITIAL_SCORE)
 
    screen.fill(BLACK)
    p1.handle_keys(1)
    p2.handle_keys(2)
    p1.draw_player(screen)
    p2.draw_player(screen)
    b.move_ball(ball_vel)
    b.draw_ball(screen)
    hud.draw_score(screen)

    # if ball hits either ends, score points and reset the ball
    if b.rect_ball.left < 0:
      hud.score_point(2)
      b = Ball()
    elif b.rect_ball.right > WIDTH:
      hud.score_point(1)
      b = Ball()

    # ball collision with player
    collide_p1 = b.rect_ball.colliderect(p1.rect_player)
    collide_p2 = b.rect_ball.colliderect(p2.rect_player)

    if collide_p1:
      ball_vel[0] = - ball_vel[0]
      b.move_ball(ball_vel)
    if collide_p2:
      ball_vel[0] = - ball_vel[0]
      b.move_ball(ball_vel)

    hud.fps_counter(clock, screen) 

    pygame.display.update() # update the screen
    clock.tick(30)

if __name__ == "__main__":
  main()