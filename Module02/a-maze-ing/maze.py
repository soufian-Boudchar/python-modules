import random
import os
import time
import sys

WIDTH = 80
HEIGHT = 30

ENTER = (0, 0)
EXIT = (79, 9)

TOP = 1
BOTTOM = 4
RIGHT = 2
LEFT = 8

SEED = 1
# random.seed(SEED)

class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = 15 # TOP: 0001 / RIGHT: 0010 / BOTTOM: 0100 / LEFT: 1000 
        self.traffic = ""
        self.visited = False


class Maze:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell(x, y) for x in range(width)] for y in range(height)]
        self.stack = []

    def get_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def check_neighbors(self, cell):
        neighbors = []

        directions = [
            (0, -1),  #Top
            (0, 1),  #Bottom
            (1, 0),  #Right
            (-1, 0)  #Left
        ]

        for dx, dy in directions:
            neighbor = self.get_cell(cell.x + dx, cell.y + dy)

            if neighbor and not neighbor.visited:
                neighbors.append(neighbor)
        return neighbors

    def remove_wall(self, current, next_cell):
        dx = next_cell.x - current.x
        dy = next_cell.y - current.y

        if dx == 1:
            current.walls -= RIGHT
            next_cell.walls -= LEFT
        elif dx == -1:
            current.walls -= LEFT
            next_cell.walls -= RIGHT
        elif dy == 1:
            current.walls -= BOTTOM
            next_cell.walls -= TOP
        elif dy == -1:
            current.walls -= TOP
            next_cell.walls -= BOTTOM
    def generate_maze(self):
        start_cell = self.grid[0][0]
        start_cell.visited = True
        self.stack.append(start_cell)

        while len(self.stack) > 0:
            current = self.stack[-1]

            neighbors = self.check_neighbors(current)

            if neighbors:
                next_cell = random.choice(neighbors)
                self.remove_wall(current, next_cell)
                next_cell.visited = True
                self.stack.append(next_cell)
            else:
                self.stack.pop()


def delete_visited(maze):
    for row in maze.grid:
        for cell in row:
            cell.visited = False

def mark_visited(cell):
    cell.visited = True


def solve_maze(maze, ENTERY, EXIT):
    start_cell = ENTERY
    end_cell = EXIT
    delete_visited(maze)

    mark_visited(start_cell)
    stack = [start_cell]

    while len(stack) > 0:
        current = stack[-1]

        if current == end_cell:
            return stack

        neighbors = []
        x = current.x
        y = current.y
        
        if y > 0 and not (current.walls & 1):  # --> check up
            neighbors.append(maze.grid[y - 1][x])
            

        if y < maze.height - 1 and not (current.walls & 4):  # --> check down
            neighbors.append(maze.grid[y + 1][x])
            
        if x < maze.width - 1 and not (current.walls & 2):  # --> check right
            neighbors.append(maze.grid[y][x + 1])
           

        if x > 0 and not (current.walls & 8):  # --> check left
            neighbors.append(maze.grid[y][x - 1])
            

        valid_neighbor = None
        for n in neighbors:
            if not n.visited:
                valid_neighbor = n
                break

        if valid_neighbor:
            mark_visited(valid_neighbor)
            stack.append(valid_neighbor)
            
            dx = valid_neighbor.x - current.x
            dy = valid_neighbor.y - current.y
            
            if dy == -1: # -> check up / North
                valid_neighbor.traffic = "N" 
            elif dy == 1:  # check down / South
                valid_neighbor.traffic = "S"
            elif dx == 1:  # check right / East
                valid_neighbor.traffic = "E"
            elif dx == -1:  # check left / West
                valid_neighbor.traffic = "W"

        else:
            stack.pop()

    return []

def draw_42(maze_grid):
        x_index_42 = (WIDTH // 2) - 3
        y_index_42 = (HEIGHT // 2) - 2
        grid_42 = [
            [0,4,5,6],
            [0,6],
            [0,1,2,4,5,6],
            [2,4],
            [2,4,5,6]
        ]

        for row_index, row in enumerate(grid_42):
            for i in row:
                maze_grid[y_index_42 + row_index][x_index_42 + i].visited = True


maze = Maze(WIDTH, HEIGHT)
draw_42(maze.grid)
maze.generate_maze()
path = solve_maze(maze, maze.grid[ENTER[1]][ENTER[0]], maze.grid[EXIT[1]][EXIT[0]])

def print_maze(maze, path):
    print()

    print("██" * (maze.width * 2 + 1))

    for y in range(len(maze.grid)):
        maze_way = "██"
        bottom = "██"

        for x in range(len(maze.grid[y])):
            cell = maze.grid[y][x]
            
            if x == EXIT[0] and y == EXIT[1]:
                maze_way += "\033[33m██\033[0m"
            elif x == ENTER[0] and y == ENTER[1]:
                maze_way += "\033[31m██\033[0m"
            elif cell in path:
                maze_way += "\033[32m██\033[0m"
            else:
                maze_way += "  "

            if cell.walls & 2:
                maze_way += "██"
            else:
                if x + 1 < maze.width:
                    right = maze.grid[y][x+1]
                    if cell in path and right in path:
                        maze_way += "\033[32m██\033[0m"
                    else:
                        maze_way += "  "
                else:
                    maze_way += "  "

            if cell.walls & 4:
                bottom += "██"
            else:
                if y + 1 < maze.height:
                    down = maze.grid[y+1][x]
                    if cell in path and down in path:
                        bottom += "\033[32m██\033[0m"
                    else:
                        bottom += "  "
                else:
                     bottom += "  "

            bottom += "██"

        print(maze_way)
        print(bottom)



def output_maze(maze, path):
    output = open("output_maze.txt", "w")

    for row in maze.grid:
        for cell in row:
            output.write(format(cell.walls, "X"))
        output.write("\n")
    output.write("\n")
    output.write(f"{ENTER[0]},{ENTER[1]}\n")
    output.write(f"{EXIT[0]},{EXIT[1]}\n")
    for cell in path:
            output.write(cell.traffic)
    output.close()

output_maze(maze, path)





tpath = []
print("\033[2J")

for _ in path[:]:
    if path:
        tpath.append(path.pop(0))

    print("\033[H", end="")
    print_maze(maze, tpath)

    sys.stdout.flush()
    time.sleep(0.01)

print("\033[H", end="")
print_maze(maze, tpath)

