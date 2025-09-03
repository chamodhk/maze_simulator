from collections import deque
from time import sleep


maze = """
..###################
......#.....#.....#.#
###.#.#.#######.###.#
#.#.#.....#...#.....#
#.###.#.#.#.###.#####
#.#...#.#...#.#.....#
#.###.###.###.###.###
#.#...#.#.....#.....#
#.#.#.#.#.###.#.#.###
#...#...#.#.#...#...#
#.###.#.#.#.#.#####.#
#.#...#.#.#.#...#...#
###.#####.#.#######.#
#...#.#...#.......#.#
#####.#.#####.#.###.#
#...#.....#.#.#.#...#
#.#.#.#####.###.###.#
#.#.....#.....#...#.#
#####.###.###.###.#.#
#.......#.#..........
###################..
"""


def get_maze_matrix(maze = maze):
    maze = maze.strip()
    maze = maze.split("\n")
    #print(len(maze))
    maze_matrix = []
    for row in maze:
        # print(row)
        row_list = []
        
        for ch in row:
            #print(ch)
            row_list.append(ch)

        maze_matrix.append(row_list)
        
        
    return maze_matrix, len(maze_matrix[0]), len(maze_matrix)

grid, grid_width, grid_height = get_maze_matrix()


def get_neighhbors(row, col):
    directions = [(0,1), (1,0), (-1, 0), (0, -1)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = row + dx, col + dy
        # print(grid_width, grid_height)
        if 0 <= nx < grid_height and 0 <= ny < grid_width:
            neighbors.append((nx, ny))


    return neighbors
    

if __name__ == "__main__":
    maze_matrix, maze_width, maze_height = get_maze_matrix(maze)
    print(maze_height, maze_width)

    print(get_neighhbors(1,1))