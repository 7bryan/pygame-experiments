import pygame, sys, random
from pygame.locals import *
#TODO : clean the code

pygame.init()

screen_width, screen_height = 800, 600

#initialize the rgb color
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


#game object
player_width, player_height = 10, 60
ai_width, ai_height = 10, 60
ball_width, ball_height = 10, 10
ball_speed_x_ori, ball_speed_y_ori = 5, 5
ball_speed_x, ball_speed_y = ball_speed_x_ori, ball_speed_y_ori
ball_speed = [ball_speed_x, ball_speed_y]

moving_up = False
moving_down = False

player  = pygame.Rect(screen_width - player_width, screen_height / 2 - player_height / 2, player_width, player_height)
ai = pygame.Rect(0, screen_height / 2 - ai_height / 2, ai_width, ai_height)
ball = pygame.Rect(screen_width / 2 - ball_width / 2, screen_height / 2 - ball_height / 2, ball_width, ball_height)

#init the font and the score text
font = pygame.font.SysFont(None, 20)
player_score = 0
ai_score = 0



clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption("ping pong game")

#handle the move of the player
def init_move(object):
    #moving the player object and stop the movement if the player object touching the edge of the screen
    global moving_up, moving_down
    if moving_up and object.top >= 0:
        object.y -= 5
    if moving_down and object.bottom <= screen_height :
        object.y += 5

        
def ai_move():
    global ai, ball
    #making sure the ai keep track of the ball position and move it based on the ball position
    if abs(ball.centery - ai.centery) > 10: #making the slight delay so the ai is beatable
        if ball.centery > ai.centery:
            ai.y += 5
        if ball.centery < ai.centery:
            ai.y -= 5
    # global ball, ai
    # ai.y = ball.y - ai_height / 2 
    
def ball_move():
    global ball, ball_speed
    ball.move_ip(ball_speed[0], ball_speed[1])
    
    #bounce the ball if it touch the screen top or bottom
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed[1] *= -1
   
    
def init_rule(paddle):
    global ball, ball_speed
    #bounce the ball if it collide with the paddle
    #mistake to correct later: sometimes the ball collide glitch with the player paddle as if the collide checking is delay or something
    if ball.colliderect(paddle):
        ball_speed[0] *= -1.05 #making the ball slightly faster from each paddle hit
        
        if ball_speed[0] > 0:  # moving right
                ball.left = paddle.right
        else:  # moving left
            ball.right = paddle.left
    
def reset_ball():
    global ball, ball_speed_x_ori, ball_speed_y_ori, ball_speed
    #reset the postion of the ball to the center of the screen
    ball.center = (screen_width // 2, screen_height // 2)
    #randomize the ball direction after reset
    new_speed_x = ball_speed_x_ori * (1 if random.randint(0, 1) else -1)
    new_speed_y = ball_speed_y_ori * (1 if random.randint(0, 1) else -1)
    ball_speed = [new_speed_x, new_speed_y]
        
def scoring():
    global player, ai, ball, player_score, ai_score
    #score if a score is scored
    
    #ai score counter
    if ball.left >= screen_width:
        ai_score += 1
        reset_ball()
        
    #player score counter
    if ball.right <= 0:
        player_score += 1
        reset_ball()
        
   

#game loop
while True:
    for event in pygame.event.get():
        #quit if quit button pressed
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
            
        if event.type == KEYDOWN:
            #add additonal event.type checking for smooth move of the player paddle
            if event.key == pygame.K_UP: #handling if and only if the key is pressed
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True
        
        if event.type == KEYUP:
            if event.key == pygame.K_UP: #handling if and only if the key is unpressed
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False
            
            
    
    #set the background color to black        
    screen.fill(black)
    
    #draw the object
    pygame.draw.rect(screen, blue, player)
    pygame.draw.rect(screen, red, ai)
    pygame.draw.rect(screen, green, ball)
    
    init_move(player)
    ball_move()
    ai_move()
    init_rule(player)
    init_rule(ai)
    scoring()
    
    #draw middle line
    pygame.draw.line(screen, red, (screen_width / 2, 0), (screen_width / 2, screen_height), 2)
    
    #draw the score
    score_text = font.render(f"score : {player_score}", True, red)
    score_text1 = font.render(f"ai score : {ai_score}", True, red)
    screen.blit(score_text, (450, 20))
    screen.blit(score_text1, (290, 20))
    
    
    
    pygame.display.update() #update the display
    clock.tick(60) #set the fps