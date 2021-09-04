from create_graph import transform_maze, create_graph
from read_write_img import read_image, write_image 
from bfs import bfs


def main():
    maze = read_image("./mazes/maze.png")

    #format the maze
    transform_maze(maze)
    
    #create graph from the maze and fint shortest path
    maze_graph = create_graph(maze)
   
    shortest_path = bfs(-1, -2, maze_graph) 

    #list with the cells that create the solution path
    shortest_path_list = [-1]    
    shortest_path_list += list(shortest_path.keys())

    write_image(maze, shortest_path_list)
    

if __name__ == "__main__":
    main()