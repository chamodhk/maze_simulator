from collections import deque
from time import sleep


maze = """  #######################################
          # #             #   # #       #
# # # ### # # ### ### ### # ### # # #####
# # # #         #   # #   # # #   #   # #
##### ######### ####### ### # # ##### # #
# #       # #   # #     #     # #   #   #
# ######### # ### ### # # # # # # ### # #
# #   # #         # # #   # # # #     # #
# # # # # ### # ### ### # # ### # ##### #
# # #   # #   #       # # # # # # #     #
# ##### # # ### # # ######### # ### #####
#     # # # # # # #     # #     # #     #
##### # # ### ##### # # # # # ### ##### #
#   #           #   # # #   # #         #
# ##### ### ##### ##### # ########### ###
# #   # # #   #   # #         #   #     #
# # # ### # # # ### # ### # ### ##### # #
#   # #   # # #     #   # # # # #   # # #
# # ##### # ### ### ######### # # ### ###
# #   #     #   #     # #         # #   #
##### ### # # # ### # # # ######### ### #
#   #   # # # # # # # #     #     #     #
# # # # # # # ### ####### ##### # ##### #
# # # # # # # #   #         # # #     # #
# ### # # # # ### ##### # ### # #########
#     # # # #       # # #   #   # # # # #
# ####### ### # # ### # ### ### # # # # #
#       #   # # #   #     #             #
### ### # ### ############### # ####### #
#   #     #   #   # #     #   #     # # #
# ##### ##### ### # ##### ### # # # # ###
# #     # #     #         #   # # #     #
####### # # # ### ####### # ########### #
#         # #         #     #     #     #
# ### # ############# # ### ### ##### ###
#   # # #     # #     # #     #   #     #
# ### ####### # ########### # # ### ### #
#   # # #           #     # # # # #   # #
####### # # ######### ### ### # # ### # #
#         #             #         #   # 
#######################################  """


def get_maze_matrix(maze = maze):
    maze = maze.split("\n")
    #print(len(maze))
    maze_matrix = []
    for row in maze:
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
        if 0 <= nx < grid_width and 0 <= ny < grid_height:
            neighbors.append((nx, ny))


    return neighbors





# def bfs_solve(maze):
#     global current_pos
#     current_pos = (0,0)
    
#     visited = set()
#     open_list = deque([current_pos])

#     while open_list:
#         current_row, current_col = open_list.popleft()
#         current_pos = (current_row, current_col)
#         # print(current_row, current_col)


#         if (current_row == 8 and current_col == 8):
#             print(open_list)

#             break
#         if ((current_row, current_col) in visited):
#             continue

#         visited.add((current_row, current_col))
#         # print(open_list)
#         # sleep(0.5)

#         for r, c in get_neighhbors(current_row, current_col):
#             print (r,c)
#             if maze[r][c] != "#" and (r,c) not in visited:
#                 open_list.append((r,c))


# bfs_solve(grid)


    
    




    

if __name__ == "__main__":
    # maze_matrix, maze_width, maze_height = get_maze_matrix(maze)
    print(get_neighhbors(1,1))