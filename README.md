# Maze-Solver

Find the shortest path in a maze with this breadth first search implementation in Python. 

## Try it out

1. Clon the repository.

```sh
git clone https://github.com/FacuEspresso/Maze-Solver.git 
```
2. Create a new virtual environment and install dependencies. 
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Leave a valid maze image at the mazes directories and run the script.

## Usage

This program takes a maze.png file, it will take each black pixel as a wall and each white one as a free path to create a matrix where 0s is a wall and a 1 is a path. For it to work, there must be an only white pixel at the first and last rows, they will be the start and end point of the maze (See the mazes/maze.png example maze ass example).

After that, it will scan and transform the matrix to set the start and end points, also, it will enumerate each free path to then create an adjacency list graph with them (This could be also done in the previous step, but i think it makes the process a bit more clearer, dividing betewen the scan of the maze image and the creation of the graph).

Finally, it runs breadth first search on the graph to find the shortest path and creates a new solved_maze.png file with the solution.
