import sys

 
def transform_maze(maze):
    '''
    recives a maze (2d array) where 0s are walls and 1s are paths
    returns the maze enumerating each path cell
    '''
    
    maze_height = len(maze)
    nodes_count = 1

    # counters to handle when the maze have more than one start or end point
    first_row_path_counter = 0
    last_row_path_counter = 0

    for r_count, row in enumerate(maze):
        for c_count, col in enumerate(row):
            # case when theres a wall
            if col != 1:
                continue

            # cases when thres a path
            # check if is the first and last row and adding the start and end
            if r_count + 1 == 1:
                maze[r_count][c_count] = -1

                first_row_path_counter += 1

                # handle case whre there is more than one start
                if first_row_path_counter > 1:
                    print("Sorry, this maze have more than one start")
                    sys.exit()

                continue
            elif r_count + 1 == maze_height:
                maze[r_count][c_count] = -2

                last_row_path_counter += 1

                # handle case whre there is more than one end
                if last_row_path_counter > 1:
                    print("Sorry, this maze have more than one end")
                    sys.exit()

                continue

            # asigns the path to nodes_count and increasing the count
            maze[r_count][c_count] = nodes_count
            nodes_count += 1

    return maze


# recives a transformed maze and returns its graph
def create_graph(t_maze):
    graph = {}

    for i in range(len(t_maze)):
        for j in range(len(t_maze[i])):
            node = t_maze[i][j]

            # when the current node isn't a wall
            if node != 0:
                temp_adj = []
                
                north_neighbor = t_maze[i-1][j]
                if north_neighbor != 0:
                    temp_adj.append(north_neighbor)

                west_neighbor = t_maze[i][j-1]
                if west_neighbor != 0:
                    #handle case when the node doesnt have neighbors at its left (negative index error)
                    if j-1 >= 0:
                        temp_adj.append(west_neighbor)
                

                #handle case where the node reaches an east wall (index error) 
                try:
                    east_neighbor = t_maze[i][j+1]
                    
                    if east_neighbor != 0:
                        temp_adj.append(east_neighbor)
                except(IndexError):
                    pass
                
                #handle case where the node reaches a south wal (index error) 
                try:
                    south_neighbor = t_maze[i+1][j]

                    if south_neighbor != 0:
                        temp_adj.append(south_neighbor)
                except(IndexError):
                    pass

                graph[node] = temp_adj

    return graph