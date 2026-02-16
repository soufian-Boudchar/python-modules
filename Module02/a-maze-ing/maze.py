import random

HEIGHT = 20
WIDTH = 20
EN = (1, 1)
EX = (9, 3)
N = 1
E = 2
S = 4
W = 8
SEED = 12312

class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = 15
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

    def remove_walls(self, current, next_cell):
        dx = next_cell.x - current.x
        dy = next_cell.y - current.y

        if dx == 1:
            current.walls -= E
            next_cell.walls -= W
        elif dx == -1:
            current.walls -= W
            next_cell.walls -= E
        elif dy == 1:
            current.walls -= S
            next_cell.walls -= N
        elif dy == -1:
            current.walls -= N
            next_cell.walls -= S
    def generate_maze(self):
        start_cell = self.grid[0][0]
        start_cell.visited = True
        self.stack.append(start_cell)

        while len(self.stack) > 0:
            current = self.stack[-1]

            neighbors = self.check_neighbors(current)

            if neighbors:

                next_cell = random.choice(neighbors)
                self.remove_walls(current, next_cell)
                next_cell.visited = True
                self.stack.append(next_cell)
            else:
                self.stack.pop()


def del_visited(maze):
    for row in maze.grid:
        for cell in row:
            cell.visited = False


def mark_visited(cell):
    cell.visited = True


def solve_maze_dfs(maze, ENTERY, EXIT):
    start_cell = ENTERY
    end_cell = EXIT
    del_visited(maze)

    mark_visited(start_cell)
    stack = [start_cell]

    while len(stack) > 0:
        current = stack[-1]

        if current == end_cell:
            return stack

        neighbors = []
        x, y = current.x, current.y

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
path = solve_maze_dfs(maze, maze.grid[EN[1]][EN[0]], maze.grid[EX[1]][EX[0]])
    
def print_maze(maze, path):
    print("+" + "---+" * WIDTH)

    for row in maze.grid:
        maze_way = "|"
        bottom = "+"
        
        for cell in row:
                
            if cell in path:
                maze_way += " o "
            else:
                maze_way += "   "

            if cell.walls & 2:
                maze_way += "|"
            else:
                maze_way += " "
            if cell.walls & 4:
                bottom += "---+"
            else:
                bottom += "   +"
        print(maze_way)
        print(bottom)



def output_maze(maze, path):
    output = open("output_maze.txt", "w")

    for row in maze.grid:
        for cell in row:
            output.write(format(cell.walls, "X"))
        output.write("\n")
    output.write("\n")
    output.write(f"{EN[0]},{EN[1]}\n")
    output.write(f"{EX[0]},{EX[1]}\n")
    for cell in path:
            output.write(cell.traffic)
    output.close()

output_maze(maze, path)
print_maze(maze, path)