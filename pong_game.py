import pygame
#Initalize Pygame
pygame.init()
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("Pong Game")

timer = pygame.time.Clock()
framerate = 60
black = (0,0,0)
white = (255,255,255)
game_over = False
font = pygame.font.Font('freesansbold.ttf',20)

#game variables
player_y = 130
computer_y = 130
ball_x = 145
ball_y = 0

player_direction = 0
player_speed = 5

ball_x_direction = 1
ball_y_direction = 1
ball_speed = 2
ball_y_speed = 2

score = 0
ball_color = white


def update_ai(ball_y, computer_y):
    computer_speed = 3
    if computer_y + 15 > ball_y + 5:
        computer_y -= computer_speed
    elif computer_y + 15 < ball_y +5:
        computer_y += computer_speed
    return computer_y

def check_collisions(ball,player, computer, ball_x_direction, score):
    if ball.colliderect(player) and ball_x_direction == -1:
        ball_x_direction = 1
        score += 1
    elif ball.colliderect(computer)and ball_x_direction == 1:
        ball_x_direction = -1
    return ball_x_direction, score

def update_ball(ball_x_direction, ball_y_direction, ball_x, ball_y, ball_speed, ball_y_speed):
    if ball_x_direction == 1 and ball_x <290:
        ball_x += ball_speed
    elif ball_x_direction == 1 and ball_x >=290:
        ball_x_direction *= -1
    if ball_x_direction == -1 and ball_x >0:
        ball_x -= ball_speed
    elif ball_x_direction == -1 and ball_x<= 0:
        ball_x_direction *= -1
   
    if ball_y_direction == 1 and ball_y <290:
        ball_y += ball_y_speed
    elif ball_y_direction == 1 and ball_y >=290:
        ball_y_direction *= -1
    if ball_y_direction == -1 and ball_y>0:
        ball_y -= ball_y_speed
    elif ball_y_direction == -1 and ball_y<= 0:
        ball_y_direction *= -1
    return ball_x_direction, ball_y_direction, ball_x, ball_y


def check_game_over(ball_x, game_over):
    if ball_x <=0 or ball_x >= 290 and game_over == False:
        game_over = True
    return game_over
   



running = True
while running:
    timer.tick(framerate)
    screen.fill(black)
    game_over = check_game_over(ball_x, game_over)
   
    player = pygame.draw.rect(screen,white,[5,player_y, 10,40])
    computer = pygame.draw.rect(screen,white,[285,computer_y, 10,40])
    ball = pygame.draw.rect(screen,ball_color, [ball_x, ball_y, 10,10])
    score_text = font.render('Score' + str(score), True, white, black)
    screen.blit(score_text, (80,30))
   
   
    if not game_over:
        computer_y = update_ai(ball_y, computer_y)
        ball_x_direction, ball_y_direction, ball_x, ball_y = update_ball(ball_x_direction, ball_y_direction, ball_x, ball_y, ball_speed, ball_y_speed)
    ball_x_direction, score = check_collisions(ball,player, computer, ball_x_direction, score)

    if game_over:
        game_over_text = font.render('Game Over', True, white, black)
        screen.blit(game_over_text, (80,130))
        restart_button = pygame.draw.rect(screen, black, [70,150,100,20])
        restart_text = font.render('Press here to restart', True, white, black)
        screen.blit(restart_text, (70,150))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_direction = -1
            if event.key == pygame.K_s:
                player_direction = 1
        if event.type == pygame.KEYUP:
            player_direction = 0
        if event.type == pygame.MOUSEBUTTONDOWN and game_over == True:
            if restart_button.collidepoint(event.pos):
                game_over = False
                player_y = 130
                computer_y = 130
                ball_x = 145
                ball_y = 0

                player_direction = 0
                player_speed = 5

                ball_x_direction = 1
                ball_y_direction = 1
                ball_speed = 2
                ball_y_speed = 2
               
                score = 0


    player_y += player_speed*player_direction
    ball_speed = 2 + (score//5)
    ball_y_speed = 1 + (score//5)
   
   
    if score >1 and score%4 == 0 and ball_x<150:
        ball_color = black
    else:
        ball_color= white
   
    pygame.display.flip()
   
pygame.quit()