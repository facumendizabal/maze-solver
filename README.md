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

This program takes a maze.png file, it will take each black pixel as a wall and each white one as a free path. For it to work, there must be an only white pixel at the first and last rows, they will be the start and end point of the maze.
