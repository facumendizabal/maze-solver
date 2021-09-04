import numpy as np
from PIL import Image, ImageDraw

WALL_COLOR = [0, 0 ,0]
FREE_PATH_COLOR = [255, 255 ,255]
SOLUTION_PATH_COLOR = [30, 80, 30]


#recives a maze img, gets its pixels and then compares each one with the wall and free_path colors.
#returns a matrix which its number of rows and columns are the width and height of the img in pixels,
#if the pixel is black, the matrix would have a 0, if it is white, the matrix would have a 1 
def read_image(img_source):
    with Image.open(img_source) as im:
        pixels = np.array(im).tolist()
        maze = []

        for row in pixels:
            temp_row = []
            for p in row:
                if p == WALL_COLOR:
                    temp_row.append(0)
                if p == FREE_PATH_COLOR:
                    temp_row.append(1)
            maze.append(temp_row)

        return maze
        
# recives a transformed maze matrix and a list with the cells that lead to the solution
# modifies the transformed matrix, if it reads a 0, it replaces it with the rgb code of the wall color,
# if the element is in the solution, with the solution color, else, with the free path color
# then creates an np array and the img
def write_image(maze, solution):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] in solution:
                maze[i][j] = SOLUTION_PATH_COLOR
            elif maze[i][j] == 0:
                maze[i][j] = WALL_COLOR
            else:
                maze[i][j] = FREE_PATH_COLOR
    
    h = len(maze)
    w = len(maze[0])

    data = np.array(maze, dtype=np.uint8)
    img = Image.fromarray(data, 'RGB')
    img.save('./mazes/solved_maze.png')