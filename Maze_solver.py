import random
from collections import deque

ROWS = 10
COLS = 10


def generate_maze():
    maze = [[random.choice([0,0,0,1]) for _ in range(COLS)] for _ in range(ROWS)]

    maze[0][0] = 0
    maze[ROWS-1][COLS-1] = 0

    return maze


def print_maze(maze, path=None):
    for i in range(ROWS):
        for j in range(COLS):

            if path and (i, j) in path:
                print("*", end=" ")

            elif maze[i][j] == 1:
                print("#", end=" ")

            elif (i, j) == (0, 0):
                print("S", end=" ")

            elif (i, j) == (ROWS-1, COLS-1):
                print("E", end=" ")

            else:
                print(".", end=" ")

        print()


def solve_maze(maze):
    start = (0, 0)
    end = (ROWS-1, COLS-1)

    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy

            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if maze[nx][ny] == 0 and (nx, ny) not in visited:

                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)

    return None


maze = generate_maze()

print("Generated Maze:\n")
print_maze(maze)

path = solve_maze(maze)

if path:
    print("\nShortest Path:\n")
    print_maze(maze, path)
else:
    print("\nNo path found")