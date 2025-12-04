import pygame
from random import randrange as rr
from settings import*

# pygame intialize
pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None, 35)
clock = pygame.time.Clock()

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(window, GREEN, [x, y, BLOCK, BLOCK])

def food_pos():
    return rr(0, WIDTH, BLOCK), rr(0, HEIGHT, BLOCK)


def game_over_screen(score):
    window.fill(BLACK)
    text1 = font.render("GAME OVER!", True, RED)
    text2 = font.render(f"Score: {score}", True, WHITE)
    text3 = font.render("Press ENTER to Play Again", True, WHITE)
    text4 = font.render("Press ESC to Quit", True, WHITE)

    window.blit(text1, (WIDTH//2 - 100, HEIGHT//2 - 80))
    window.blit(text2, (WIDTH//2 - 70, HEIGHT//2 - 30))
    window.blit(text3, (WIDTH//2 - 180, HEIGHT//2 + 20))
    window.blit(text4, (WIDTH//2 - 150, HEIGHT//2 + 60))

    pygame.display.update()

    # Wait for input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # ENTER
                    game_loop()
                if event.key == pygame.K_ESCAPE:  # ESC
                    pygame.quit()
                    quit()

# main loop
def game_loop():
    snake_x, snake_y= int(WIDTH/2), int(HEIGHT/2)
    food_x, food_y = food_pos()

    direction = ''

    snake_list = []
    snake_size = 1
    score = 0
    text = f"Score: {score}"

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                quit() 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d and direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP or event.key == pygame.K_w and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s and direction != 'UP':
                    direction = 'DOWN'
        
        if direction == 'LEFT':
            snake_x -= SPEED
        elif direction == 'RIGHT':
            snake_x += SPEED
        elif direction == 'UP':
            snake_y -= SPEED
        elif direction == 'DOWN':
            snake_y += SPEED

        if snake_x < 0:
            snake_x += WIDTH
        elif snake_x > WIDTH:
            snake_x -= WIDTH
        elif snake_y < 0:
            snake_y += HEIGHT
        elif snake_y > HEIGHT:
            snake_y -= HEIGHT

        #snake Size control
        snake_head = [snake_x, snake_y]

        if snake_head in snake_list and direction != '':
            game_over_screen(score)

        snake_list.append(snake_head)
        if len(snake_list) > snake_size:
            del snake_list[0]

        # Food eating and create
        if [food_x, food_y] in snake_list:
            food_x, food_y = food_pos()
            score += 1
            snake_size += 1
        

        # Draw section
        window.fill(BLACK)

        text = f"Score: {score}"
        score_surface = font.render(text, True, WHITE)
        window.blit(score_surface, (20, 20))
        
        draw_snake(snake_list)
        pygame.draw.rect(window, RED, [food_x, food_y, BLOCK, BLOCK])
        pygame.display.update()




# Game Runner
game_loop()