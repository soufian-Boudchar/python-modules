import random
import os
import time
import sys
from collections import deque

THEMES = {
    "electric_arctic": {
        "background": "\033[48;2;11;19;43m  \033[0m",
        "walls":      "\033[48;2;58;80;107m  \033[0m",
        "path":       "\033[48;2;255;255;255m  \033[0m",
        "enter":      "\033[48;2;111;255;233m  \033[0m",
        "exit":       "\033[48;2;255;0;85m  \033[0m",
        "logo":       "\033[48;2;0;229;255m  \033[0m"
    },
    "sanguine_horizon": {
        "background": "\033[48;2;10;2;2m  \033[0m",
        "walls":      "\033[48;2;102;0;0m  \033[0m",
        "path":       "\033[48;2;255;179;179m  \033[0m",
        "enter":      "\033[48;2;255;215;0m  \033[0m",
        "exit":       "\033[48;2;255;255;255m  \033[0m",
        "logo":       "\033[48;2;255;77;109m  \033[0m"
    },
    "sunlight_in_the_cave": {
        "background": "\033[48;2;26;18;11m  \033[0m",
        "walls":      "\033[48;2;99;68;50m  \033[0m",
        "path":       "\033[48;2;255;244;224m  \033[0m",
        "enter":      "\033[48;2;234;182;118m  \033[0m",
        "exit":       "\033[48;2;55;48;107m  \033[0m",
        "logo":       "\033[48;2;212;163;115m  \033[0m"
    },
    "ghostly_lavender": {
        "background": "\033[48;2;22;16;50m  \033[0m",
        "walls":      "\033[48;2;84;94;117m  \033[0m",
        "path":       "\033[48;2;232;215;255m  \033[0m",
        "enter":      "\033[48;2;157;80;187m  \033[0m",
        "exit":       "\033[48;2;0;255;209m  \033[0m",
        "logo":       "\033[48;2;183;148;244m  \033[0m"
    },
    "industrial_lime": {
        "background": "\033[48;2;18;18;18m  \033[0m",
        "walls":      "\033[48;2;102;102;102m  \033[0m",
        "path":       "\033[48;2;244;255;153m  \033[0m",
        "enter":      "\033[48;2;255;87;51m  \033[0m",
        "exit":       "\033[48;2;51;255;87m  \033[0m",
        "logo":       "\033[48;2;167;255;131m  \033[0m"
    },
    "desert_rose": {
        "background": "\033[48;2;45;36;36m  \033[0m",
        "walls":      "\033[48;2;140;106;106m  \033[0m",
        "path":       "\033[48;2;254;236;226m  \033[0m",
        "enter":      "\033[48;2;234;182;118m  \033[0m",
        "exit":       "\033[48;2;92;61;46m  \033[0m",
        "logo":       "\033[48;2;255;143;163m  \033[0m"
    }
}




WIDTH = 35
HEIGHT = 15

ENTER = (0, 0)
EXIT = (34,  14)

TOP = 1
BOTTOM = 4
RIGHT = 2
LEFT = 8

SEED = 42
random.seed(SEED)

# theme_name = random.choice(list(THEMES.keys()))
theme = THEMES["electric_arctic"]
class Cell:

    def __init__(self, row: int, col: int, size=0):
        self.__row = row
        self.__col = col
        self.__size = size
        self.__top = True
        self.__right = True
        self.__bottom = True
        self.__left = True
        self.__cell_42 = False
        self.__visited = False
        self.traffic = ""

    @property
    def cell_42(self) -> bool:
        return self.__cell_42

    @cell_42.setter
    def cell_42(self, value: bool) -> None:
        self.__cell_42 = value

    @property
    def row(self) -> int:
        return self.__row

    @property
    def col(self) -> int:
        return self.__col

    @property
    def size(self) -> int:
        return self.__size

    @property
    def top(self) -> bool:
        return self.__top

    @top.setter
    def top(self, top) -> None:
        self.__top = top

    @property
    def right(self) -> bool:
        return self.__right

    @right.setter
    def right(self, right) -> None:
        self.__right = right

    @property
    def bottom(self) -> bool:
        return self.__bottom

    @bottom.setter
    def bottom(self, bottom) -> None:
        self.__bottom = bottom

    @property
    def left(self) -> bool:
        return self.__left

    @left.setter
    def left(self, left) -> None:
        self.__left = left

    @property
    def visited(self) -> bool:
        return self.__visited

    @visited.setter
    def visited(self, value) -> None:
        self.__visited = value
    
class Maze:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[Cell(y, x) for x in range(width)] for y in range(height)]
        self.stack = []
        
    def get_cell(self, col: int, row: int):
        if 0 <= col < self.width and 0 <= row < self.height:
            return self.grid[row][col]
        return None

    def check_neighbors(self, cell: Cell):
        neighbors = []

        directions = [
            (0, -1),  #Top
            (0, 1),  #Bottom
            (1, 0),  #Right
            (-1, 0)  #Left
        ]

        for dx, dy in directions:
            neighbor = self.get_cell(cell.col + dx, cell.row + dy)

            if neighbor and not neighbor.visited:
                neighbors.append(neighbor)
        return neighbors

    def remove_wall(self, current: Cell, next_cell: Cell):
        dx = next_cell.col - current.col
        dy = next_cell.row - current.row

        if dx == 1:
            current.right = False
            next_cell.left = False
        elif dx == -1:
            current.left = False
            next_cell.right = False
        elif dy == 1:
            current.bottom = False
            next_cell.top = False
        elif dy == -1:
            current.top = False
            next_cell.bottom = False

    def generate_maze(self, theme: dict, animation=False):
        stack = []
        start_cell = self.grid[0][0]
        start_cell.visited = True
        stack.append(start_cell)
        
        if animation: # (tui)
            print("\033[?25l", end="")
            print("\033[H", end="")
            print_maze(self, [], theme)
            # get the cordinate of cell (Tui)
            def draw_block(x, y, char, dx=0, dy=0):
                row = 2 + y * 2 + dy
                col = 3 + x * 4 + (dx * 2)
                print(f"\033[{row};{col}H{char}", end="")


        while len(stack) > 0:
            current = stack[-1]
            neighbors = self.check_neighbors(current)

            if neighbors:
                next_cell = random.choice(neighbors)
                self.remove_wall(current, next_cell)
                next_cell.visited = True
                stack.append(next_cell)

                if animation:
                    draw_block(current.col, current.row, theme['background'])
                    draw_block(current.col, current.row, theme['background'], next_cell.col - current.col, next_cell.row - current.row)
                    draw_block(next_cell.col, next_cell.row, "\033[38;5;196m██\033[0m")
                    draw_block(ENTER[0], ENTER[1], theme["enter"])
                    draw_block(EXIT[0], EXIT[1], theme["exit"])
                    sys.stdout.flush()
                    time.sleep(0.01)
            else:
                if animation:
                    popped = stack.pop()
                    draw_block(popped.col, popped.row, theme['background'])
                    sys.stdout.flush()
                    time.sleep(0.005)
                else:
                    stack.pop()

        print("\033[?25h", end="")



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
        col = current.col
        row = current.row

        if row > 0 and current.top == False:  # --> check up
            neighbors.append(maze.grid[row - 1][col])

        if row < maze.height - 1 and current.bottom == False:  # --> check down
            neighbors.append(maze.grid[row + 1][col])

        if col < maze.width - 1 and current.right == False:  # --> check right
            neighbors.append(maze.grid[row][col + 1])

        if col > 0 and current.left == False:  # --> check left
            neighbors.append(maze.grid[row][col - 1])

        valid_neighbor = None
        for n in neighbors:
            if not n.visited:
                valid_neighbor = n
                break

        if valid_neighbor:
            mark_visited(valid_neighbor)
            stack.append(valid_neighbor)

            dx = valid_neighbor.col - current.col
            dy = valid_neighbor.row - current.row
            if dy == -1:  # -> check up / North
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


def draw_42(maze_grid: list[list[Cell]]):
    x_index_42 = (WIDTH // 2) - 3
    y_index_42 = (HEIGHT // 2) - 2
    grid_42 = [[0, 4, 5, 6], [0, 6], [0, 1, 2, 4, 5, 6], [2, 4], [2, 4, 5, 6]]

    for row_index, row in enumerate(grid_42):
        for i in row:
            maze_grid[y_index_42 + row_index][x_index_42 + i].visited = True

    


def print_maze(maze: Maze, path: list[Cell], theme: dict):
    print(f"{theme['walls']}" * (maze.width * 2 + 1))
    for y in range(len(maze.grid)):
        maze_way = f"{theme['walls']}"
        bottom = f"{theme['walls']}"

        for x in range(len(maze.grid[y])):
            cell = maze.grid[y][x]

            #Center logic
            if x == EXIT[0] and y == EXIT[1]:
                maze_way += f"{theme['exit']}"
            elif x == ENTER[0] and y == ENTER[1]:
                maze_way += f"{theme['enter']}"
            elif cell in path:
                maze_way += f"{theme['path']}"

            elif cell.top and cell.right and cell.left and cell.bottom:
                maze_way += f"{theme['logo']}"

            else:
                maze_way += theme['background']


            #Right logic
            if cell.right:
                maze_way += f"{theme['walls']}"
            else:
                if x + 1 < maze.width:
                    right = maze.grid[y][x + 1]
                    if cell in path and right in path:
                        maze_way += f"{theme['path']}"
                    else:
                        maze_way += theme['background']
                else:
                    maze_way += theme['background']
            #Bottom logic
            if cell.bottom:
                bottom += f"{theme['walls']}"
            else:
                if y + 1 < maze.height:
                    down = maze.grid[y + 1][x]
                    if cell in path and down in path:
                        bottom += f"{theme['path']}"
                    else:
                        bottom += theme['background']
                else:
                    bottom += theme['background']

            bottom += f"{theme['walls']}"

        print(maze_way)
        print(bottom)


def output_maze(maze, path):
    output = open("output_maze.txt", "w")

    for row in maze.grid:
        for cell in row:
            walls = 0
            if cell.top:
                walls += 1
            if cell.right:
                walls += 2
            if cell.bottom:
                walls += 4
            if cell.left:
                walls += 8
            output.write(format(walls, "X"))

        output.write("\n")
    output.write("\n")
    output.write(f"{ENTER[0]},{ENTER[1]}\n")
    output.write(f"{EXIT[0]},{EXIT[1]}\n")
    for cell in path:
        output.write(cell.traffic)
    output.close()

def path_animating(maze, path, theme):
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[?25l", end="")
    print("\033[H", end="")

    print_maze(maze, [], theme)

    def draw_path_block(x, y, char, dx=0, dy=0):
        row = 2 + y * 2 + dy 
        col = 3 + x * 4 + (dx * 2)
        print(f"\033[{row};{col}H{char}", end="")
    for i in range(len(path)):
        cell = path[i]
        if i > 0:
            prev = path[i - 1]
            draw_path_block(prev.col, prev.row, theme['path'], cell.col - prev.col, cell.row - prev.row)
        draw_path_block(cell.col, cell.row, theme['path'])
        sys.stdout.flush()
        draw_path_block(ENTER[0], ENTER[1], theme["enter"])
        draw_path_block(EXIT[0], EXIT[1], theme["exit"])
        time.sleep(0.01)
    print("\033[H", end="")

    print_maze(maze, path, theme)
    print("\033[?25h", end="") # enable cursor


def main(theme):
    parameters = {
        "animation": False,
        "show_path": False
    }
    GREEN = "\033[32m"
    RED = "\033[31m"
    RESET = "\033[0m"
    print("\033[?25l", end="")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[H", end="")
    maze = Maze(WIDTH, HEIGHT)
    draw_42(maze.grid)
    maze.generate_maze(theme)
    path = solve_maze(maze, maze.grid[ENTER[1]][ENTER[0]], maze.grid[EXIT[1]][EXIT[0]])
    print_maze(maze, [], theme)

    while True:
        path = solve_maze(maze, maze.grid[ENTER[1]][ENTER[0]], maze.grid[EXIT[1]][EXIT[0]])
        # os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[H", end="")
        if parameters["show_path"]:
            print_maze(maze, path, theme)
        else:
            print_maze(maze, [], theme)
        print("\n1. Regenerate maze")
        if parameters["show_path"]:
            print(f"2. ON/OFF path  [{GREEN + 'ON' + RESET}]")
        else:
            print(f"2. ON/OFF path [{RED + 'OFF' + RESET}]")
        if parameters["animation"]:
            print(f"3. ON/OFF Animation  [{GREEN + 'ON' + RESET}]")
        else:
            print(f"3. ON/OFF Animation [{RED + 'OFF' + RESET}]")
        print("4. Shuffle colors")
        print("5. Exit")
        output_maze(maze, path)
        user_in = int(input("\nEnter your choice: "))


        if user_in == 1: # Regenerate
            print("\033[H", end="")
            maze = Maze(WIDTH, HEIGHT)
            draw_42(maze.grid)

            if parameters["animation"] and parameters["show_path"]:
                maze.generate_maze(theme, True)
                path = solve_maze(maze, maze.grid[ENTER[1]][ENTER[0]], maze.grid[EXIT[1]][EXIT[0]])
                print("\033[H", end="")
                path_animating(maze, path, theme)

            elif not parameters["animation"] and parameters["show_path"]:
                maze.generate_maze(theme)
                path = solve_maze(maze, maze.grid[ENTER[1]][ENTER[0]], maze.grid[EXIT[1]][EXIT[0]])
                print("\033[H", end="")
                print_maze(maze, path, theme)

            elif parameters["animation"] and not parameters["show_path"]:
                maze.generate_maze(theme, True)
                path = solve_maze(maze, maze.grid[ENTER[1]][ENTER[0]], maze.grid[EXIT[1]][EXIT[0]])
                print("\033[H", end="")
                print_maze(maze, [], theme)

            elif not parameters["animation"] and not parameters["show_path"]:
                maze.generate_maze(theme)
                print("\033[H", end="")
                print_maze(maze, [], theme)
            path = solve_maze(maze, maze.grid[ENTER[1]][ENTER[0]], maze.grid[EXIT[1]][EXIT[0]])
            output_maze(maze, path)


        elif user_in == 2: # Show/Hide path
            print("\033[H", end="")
            if parameters["show_path"]:
                # os.system('cls' if os.name == 'nt' else 'clear')
                
                print("\033[H", end="")
                print_maze(maze, [], theme)
                parameters["show_path"] = False
                
            elif not parameters["show_path"] and not parameters["animation"]:
                # os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[H", end="")
                print_maze(maze, path, theme)
                parameters["show_path"] = True
                
            elif not parameters["show_path"] and parameters["animation"]:
                print("\033[H", end="")
                path_animating(maze, path, theme)
                parameters["show_path"] = True
    
        elif user_in == 3: # Animating
            # os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[H", end="")
            if parameters["show_path"]:
                print_maze(maze, path, theme)
            else:
                print_maze(maze, [], theme)
            if parameters["animation"] == False:
                parameters["animation"] = True
            elif parameters["animation"] == True:
                parameters["animation"] = False
                

        elif user_in == 4: # shuffle colors
            # os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[H", end="")
            
            theme_name = random.choice(list(THEMES.keys()))
            theme = THEMES[theme_name]
            if parameters["show_path"]:
                print_maze(maze, path, theme)
            else:
                print_maze(maze, [], theme)
            
        elif user_in == 5:
            print("\033[?25h", end="")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[H")
            exit()
        print("\033[?25h", end="")

    
    # maze_animating(maze, path)
main(theme)


# maze = Maze(WIDTH, HEIGHT)
# draw_42(maze.grid)
# os.system('clear')
# maze.generate_maze(theme)
# path = solve_maze(maze, maze.grid[ENTER[1]][ENTER[0]], maze.grid[EXIT[1]][EXIT[0]])
# print_maze(maze, path, theme, None, None)
# print(theme_name)
