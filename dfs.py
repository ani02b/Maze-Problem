import time

def read_maze(file_name):
    maze = []
    with open(file_name, 'r') as file:
        for line in file:
            maze.append(list(line.strip()))
    return maze

def get_neighbors(maze, row, col):
    neighbors = []
    directions = [(0, 1, 'Right'), (0, -1, 'Left'), (1, 0, 'Down'), (-1, 0, 'Up')]  # Right, Left, Down, Up

    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != '#':
            neighbors.append((new_row, new_col, direction[2]))

    return neighbors

def solve_maze(maze, current, goal, visited, path):
    row, col = current

    if current == goal:
        return True
    if current in visited:
        return False

    visited.add(current)

    neighbors = get_neighbors(maze, row, col)

    for neighbor in neighbors:
        if solve_maze(maze, neighbor[:2], goal, visited, path):
            path.append(neighbor[2])
            return True

    return False

def main():
    begin=time.time()

    maze = read_maze('maze.txt') # read other maze files and test for them

    start = None
    goal = None

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'G':
                goal = (i, j)

    visited = set()
    path = []

    if solve_maze(maze, start, goal, visited, path):
        print("Path found:")
        path.reverse()
        for step in path:
            print(step)
    else:
        print("No path found.")
    
    end=time.time()
    print("Execution time= ",(end-begin)*(10**3),"ms")

# Run the main function
if __name__ == '__main__':
    main()
