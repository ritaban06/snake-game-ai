import pygame
import random
import numpy as np
from collections import deque

# Initialize Pygame
pygame.init()

# Set up the game window
width = 1400
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Enhanced Snake Game AI")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Game parameters
snake_block = 20
snake_speed = 15
obstacle_count = 10
power_up_duration = 50  # frames

# Initialize clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 30)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    window.blit(mesg, [10, 10])

def bfs(start, goal, grid):
    queue = deque([[start]])
    visited = set([start])
    
    while queue:
        path = queue.popleft()
        y, x = path[-1]
        
        if (y, x) == goal:
            return path
        
        for y2, x2 in ((y+1,x), (y-1,x), (y,x+1), (y,x-1)):
            if (0 <= y2 < grid.shape[0] and 0 <= x2 < grid.shape[1] and 
                grid[int(y2)][int(x2)] != 1 and (y2, x2) not in visited):
                queue.append(path + [(y2, x2)])
                visited.add((y2, x2))
    
    return None

def ai_make_decision(x1, y1, foodx, foody, snake_list, obstacles, power_up):
    grid = np.zeros((height // snake_block, width // snake_block))
    
    for segment in snake_list:
        grid[int(segment[1] // snake_block)][int(segment[0] // snake_block)] = 1
    
    for obs in obstacles:
        grid[int(obs[1] // snake_block)][int(obs[0] // snake_block)] = 1
    
    path = bfs((y1 // snake_block, x1 // snake_block), 
               (foody // snake_block, foodx // snake_block), 
               grid)
    
    if power_up:
        path_to_power_up = bfs((y1 // snake_block, x1 // snake_block), 
                               (power_up[1] // snake_block, power_up[0] // snake_block), 
                               grid)
        if path_to_power_up and (not path or len(path_to_power_up) < len(path)):
            path = path_to_power_up
    
    if path:
        next_move = path[1]
        dx = (next_move[1] * snake_block) - x1
        dy = (next_move[0] * snake_block) - y1
        return dx, dy, path
    else:
        possible_moves = [
            (snake_block, 0), (-snake_block, 0), (0, snake_block), (0, -snake_block)
        ]
        for move in possible_moves:
            new_x = x1 + move[0]
            new_y = y1 + move[1]
            if (0 <= new_x < width and 0 <= new_y < height and 
                [new_x, new_y] not in snake_list and [new_x, new_y] not in obstacles):
                return move[0], move[1], None
        
        return 0, 0, None

def gameLoop():
    game_over = False
    x1 = width // 2
    y1 = height // 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    score = 0
    power_up_active = 0

    foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

    obstacles = [[round(random.randrange(0, width - snake_block) / snake_block) * snake_block,
                  round(random.randrange(0, height - snake_block) / snake_block) * snake_block]
                 for _ in range(obstacle_count)]

    power_up = None
    power_up_timer = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        x1_change, y1_change, path = ai_make_decision(x1, y1, foodx, foody, snake_list, obstacles, power_up)

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True
            break

        x1 += x1_change
        y1 += y1_change
        window.fill(BLACK)
        
        # Draw obstacles
        for obs in obstacles:
            pygame.draw.rect(window, BLUE, [obs[0], obs[1], snake_block, snake_block])
        
        # Draw food
        pygame.draw.rect(window, RED, [foodx, foody, snake_block, snake_block])
        
        # Draw power-up
        if power_up:
            pygame.draw.rect(window, YELLOW, [power_up[0], power_up[1], snake_block, snake_block])
        
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        our_snake(snake_block, snake_list)
        
        # Draw path
        if path:
            for node in path[1:]:
                pygame.draw.rect(window, (100, 100, 100), 
                                 [node[1]*snake_block, node[0]*snake_block, snake_block, snake_block], 1)

        if power_up_active > 0:
            message(f"Score: {score} - POWER UP!", YELLOW)
            power_up_active -= 1
        else:
            message(f"Score: {score}", WHITE)
        
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
            length_of_snake += 1
            score += 1
            
            # Spawn power-up
            if random.random() < 0.3 and not power_up:  # 30% chance to spawn power-up
                power_up = [round(random.randrange(0, width - snake_block) / snake_block) * snake_block,
                            round(random.randrange(0, height - snake_block) / snake_block) * snake_block]

        if power_up and x1 == power_up[0] and y1 == power_up[1]:
            power_up = None
            power_up_active = power_up_duration
            score += 5

        clock.tick(snake_speed)

    # Show the last frame
    message("Game Over! Final Score: " + str(score), WHITE)
    pygame.display.update()
    
    # Wait for a few seconds before quitting
    pygame.time.wait(3000)
    
    pygame.quit()
    quit()

# Start the game
gameLoop()