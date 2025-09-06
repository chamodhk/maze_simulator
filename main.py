import pygame
from maze_handler import get_maze_matrix, get_neighhbors
from collections import deque



maze, maze_width, maze_height  = get_maze_matrix()

WIDTH = 720
HEIGHT = 720

cell_width = float(WIDTH/maze_width) 



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Simulator")
clock = pygame.time.Clock()

running = True

start_pos = (0,0)
open_list = deque([start_pos])
visited = set()
visited.add(start_pos)


Rat = pygame.Rect(0, 0, cell_width,cell_width)

end_pos = (maze_height - 1, maze_width - 1)

#
def draw_rat(screen):
    global found
    if open_list:


        current_pos = open_list.popleft()
        if current_pos == end_pos:
            found = True 
            print(len(visited), maze_height*maze_width)
            get_path()
            visited.clear()

            print("break")
            return


        visited.add(current_pos)

        for neighbor in get_neighhbors(current_pos[0],current_pos[1]):
        
            if  neighbor not in visited and maze[neighbor[0]][neighbor[1]] != "#":
                # visited.add(neighbor)
                parents[neighbor] = current_pos
                open_list.append(neighbor)
                


    Rat = pygame.Rect((current_pos[1]*cell_width, current_pos[0]*cell_width, cell_width, cell_width))

    pygame.draw.rect(screen,"red", Rat)


parents = {
    start_pos : None
}

path = []
def get_path():
    node = end_pos
    while(parents[node]):
        path.append(node)
        node = parents[node]



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
            Box = pygame.Rect(y1, x1, y2 - y1, x2 - x1)
            # print(cell)
            if cell == ".":
                pygame.draw.rect(screen, "black", Box)

            else:
        
                pygame.draw.rect(screen, "white", Box)

            if (i,j) in visited:
                pygame.draw.rect(screen, "blue", Box)

def draw_path(screen):
    for i, j in path:
        x1 = round(i * cell_width)
        x2 =round( (i + 1) * cell_width)
        y1 = round(j * cell_width)
        y2 = round((j + 1) * cell_width)
        pygame.draw.rect(screen, "red", pygame.Rect(y1, x1, y2- y1, x2 - x1))


found = False
# draw_maze(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    #draw_grid(screen)
    draw_maze(screen)
    if not found:
        draw_rat(screen)
    else:
        draw_path(screen)


    pygame.display.flip()

    # clock.tick(1200)

pygame.quit() 