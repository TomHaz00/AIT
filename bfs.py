def bfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = [(start[0], start[1], 0)]  # Open list
    visited = []  # Visited list
    visited.append(start)

    while queue:
        x, y, distance = queue.pop(0)

        if (x, y) == goal:
            return distance, visited, queue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.append((nx, ny))
                queue.append((nx, ny, distance + 1))

    return -1, visited, queue


grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0]
]

start = (0, 0)
goal = (4, 4)

distance, visited, queue = bfs(grid, start, goal)

if distance != -1:
    print(f"Nejkratší cesta od startu k cíli má {distance} kroků ^^")
else:
    print("Nejde se dostat do cíle cigáne >:(")

print("\nVisited positions:")
print(visited)

print("\nOpen list (positions in queue):")
print(queue)
