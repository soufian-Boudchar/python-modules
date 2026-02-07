import random

WIDTH = 15
HEIGHT = 9
grid = [[15 for x in range(WIDTH)] for y in range(HEIGHT)]

NORTH = 1
SOUTH = 4
EAST = 2
WEST = 8


def remove_walls(current_x, current_y, next_x, next_y, grid):
    dx = next_x - current_x
    dy = next_y - current_y

    if dx == 1:
        grid[current_y][current_x] -= EAST
        grid[next_y][next_x] -= WEST
    elif dx == -1:
        grid[current_y][current_x] -= WEST
        grid[next_y][next_x] -= EAST
    elif dy == 1:
        grid[current_y][current_x] -= SOUTH
        grid[next_y][next_x] -= NORTH
    elif dy == -1:
        grid[current_y][current_x] -= NORTH
        grid[next_y][next_x] -= SOUTH


def get_valid_neighbors(x, y, visited):
    neighbors = []
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy

        if (0 <= new_x < WIDTH) and (0 <= new_y < HEIGHT):
            if (new_x, new_y) not in visited:
                neighbors.append((new_x, new_y))
    return neighbors


start_cell = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
visited = [start_cell]
stack = [start_cell]

while len(stack) > 0:
    current_x, current_y = stack[-1]

    neighbors = get_valid_neighbors(current_x, current_y, visited)

    if len(neighbors) > 0:
        next_cell = random.choice(neighbors)
        next_x, next_y = next_cell

        remove_walls(current_x, current_y, next_x, next_y, grid)

        visited.append(next_cell)
        stack.append(next_cell)
    else:
        stack.pop()


def draw_maze(grid):
    h = len(grid)
    w = len(grid[0])

    print("O" + "oooO" * w)

    for y in range(h):
        line_walls = "│"
        line_bottom = "o"

        for x in range(w):
            cell = grid[y][x]

            line_walls += "   "

            if cell & 2:
                line_walls += "│"
            else:
                line_walls += " "

            if cell & 4:
                line_bottom += "oooO"
            else:
                line_bottom += "   O"

        print(line_walls)
        print(line_bottom)
draw_maze(grid)
