# main.py
# Austin Sohn, Ethan Luu

import sys, pygame, random

DEFAULT_PLAYER_SIZE = (10,75) # width, height
DEFAULT_BALL_SIZE = (15,15) # width, height
SIZE = WIDTH, HEIGHT = 800, 600
INITIAL_SCORE = [0, 0]
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Players(object):
  def __init__(self, spawn):
    self.image_rectangle = pygame.image.load("./pong_images/white_rectangle.jpg")
    self.player = pygame.transform.scale(self.image_rectangle, DEFAULT_PLAYER_SIZE)
    self.x = spawn[0]
    self.y = spawn[1]
    self.rect_player = pygame.Rect(self.x,self.y,DEFAULT_PLAYER_SIZE[0],DEFAULT_PLAYER_SIZE[1])
    self.player_vel = 10

  def handle_keys(self, direction):
    # if player hits top or bottom edge, stop them from continuing
    if self.rect_player.y <= 0:
      self.rect_player.y = 0 
    elif self.rect_player.y >= HEIGHT-DEFAULT_PLAYER_SIZE[1]:
      self.rect_player.y = HEIGHT-DEFAULT_PLAYER_SIZE[1]

  # Handles Keys
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and direction== 1: # w = player1 up
      self.rect_player.y -= self.player_vel
    elif key[pygame.K_s] and direction == 1: # s = player1 down
      self.rect_player.y += self.player_vel
    if key[pygame.K_o] and direction == 2: # o = player2 up
      self.rect_player.y -= self.player_vel
    elif key[pygame.K_l] and direction == 2: # l = player2 down
      self.rect_player.y += self.player_vel

  def draw_player(self, surface):
   pygame.draw.rect(surface, WHITE, self.rect_player); 

class Ball(object):
  def __init__(self):
    image_ball = pygame.image.load("./pong_images/white_circle.png")
    self.ball = pygame.transform.scale(image_ball, DEFAULT_BALL_SIZE)
    self.x = WIDTH/2
    self.y = HEIGHT/2
    self.rect_ball = pygame.Rect(self.x,self.y,DEFAULT_BALL_SIZE[0],DEFAULT_BALL_SIZE[1])
    self.ball_speed = 7
    self.ball_start_x = random.choice((-self.ball_speed, self.ball_speed))
    self.ball_start_y = random.choice((-self.ball_speed, self.ball_speed))
    self.ball_vel = [self.ball_start_x, self.ball_start_y]

  def draw_ball(self, surface):
    pygame.draw.ellipse(surface, WHITE, self.rect_ball); 

  def move_ball(self):
    self.x += self.ball_vel[0]
    self.y += self.ball_vel[1]
    self.rect_ball.topleft = (self.x, self.y)
    # if ball hits top or bottom wall, bounce back down
    if self.rect_ball.top < 0 or self.rect_ball.bottom > HEIGHT:
      self.ball_vel[1] = -self.ball_vel[1]

  def collision_ball(self, p):
    # if ball hits player, send it back
    if p == 1:
      self.ball_vel[0] = - self.ball_vel[0]
      self.move_ball()
    if p == 2:
      self.ball_vel[0] = - self.ball_vel[0]
      self.move_ball()

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
  p1Spawn = [10,HEIGHT/2]
  p2Spawn=[WIDTH-10-DEFAULT_PLAYER_SIZE[0], HEIGHT/2]
  p1 = Players(p1Spawn)
  p2 = Players(p2Spawn)
  b = Ball()
  hud = HUD(INITIAL_SCORE)
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT: sys.exit()
      if event.type == pygame.KEYDOWN: 
        # exits game if you press q
        if event.key == pygame.K_q: 
          sys.exit()
        # resets game if you press space or r
        elif event.key == pygame.K_SPACE or event.key == pygame.K_r: 
          p1 = Players(p1Spawn)
          p2 = Players(p2Spawn)
          b = Ball()
          hud = HUD(INITIAL_SCORE)
 
    screen.fill(BLACK)
    p1.handle_keys(1)
    p2.handle_keys(2)
    p1.draw_player(screen)
    p2.draw_player(screen)
    b.move_ball()
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
      b.collision_ball(collide_p1)
    if collide_p2:
      b.collision_ball(collide_p2)

    # show fps counter
    # hud.fps_counter(clock, screen) 

    # update the screen
    pygame.display.update() 
    # tickrate
    clock.tick(30)

if __name__ == "__main__":
  main()