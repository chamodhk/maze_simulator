import pygame
from maze_handler import get_maze_matrix, get_neighhbors
from collections import deque
from time import sleep

maze, maze_width, maze_height  = get_maze_matrix()

WIDTH = 720
HEIGHT = 720

cell_width = float(WIDTH/maze_width) 
print(cell_width)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Simulator")
clock = pygame.time.Clock()

running = True

start_pos = (0,0)
open_list = deque([start_pos])
visited = set()
visited.add(start_pos)


Rat = pygame.Rect(0, 0, 20,20)


found = False
def draw_rat(screen):
    current_pos = open_list.popleft()
    # print(current_pos)
    # sleep(0.5)

    if current_pos[0] == 39 and current_pos == 39:
        found = True 
        print("break")
        return


    visited.add(current_pos)

    for neighbor in get_neighhbors(current_pos[0],current_pos[1]):
        # print(neighbor)
        if  neighbor not in visited and maze[neighbor[0]][neighbor[1]] != "#":
            # visited.add(neighbor)
            open_list.append(neighbor)
            


    Rat = pygame.Rect((current_pos[0]*cell_width, current_pos[1]*cell_width, 20, 20))

    pygame.draw.rect(screen,"red", Rat)

def draw_grid(screen):
    # cell_width = (cell_width + cell_height )/2
    for i in range(1, maze_width):
        line = pygame.Rect(int(i * cell_width), 0, 1, HEIGHT)
        pygame.draw.rect(screen, "white", line)

    for i in range(1, maze_width):
        line = pygame.Rect(0, i * cell_width,  WIDTH, 1)
        pygame.draw.rect(screen, "white", line)
        
    
def draw_maze(screen, maze= maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            x1 = round(i * cell_width)
            x2 =round( (i + 1) * cell_width)
            y1 = round(j * cell_width)
            y2 = round((j + 1) * cell_width)
            Box = pygame.Rect(x1, y1,y2 - y1, x2 - x1)
            # print(cell)
            if cell == " ":
                pygame.draw.rect(screen, "black", Box)

            else:
        
                pygame.draw.rect(screen, "white", Box)

            if (i,j) in visited:
                pygame.draw.rect(screen, "blue", Box)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    #draw_grid(screen)
    draw_maze(screen)
    if not found:
        draw_rat(screen)

    pygame.display.flip()

    clock.tick(1000)

pygame.quit() 