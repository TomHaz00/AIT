from collections import deque


def rescue_vehicle(grid, R, C, F, start, target):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0, 0)])
    visited = [[[False] * (F + 1) for _ in range(C)] for _ in range(R)]
    visited[start[0]][start[1]][0] = True

    while queue:
        r, c, steps, danger = queue.popleft()

        if (r, c) == target:
            return steps

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                new_danger = danger + (1 if grid[nr][nc] == 1 else 0)
                if new_danger <= F and not visited[nr][nc][
                    new_danger]:
                    visited[nr][nc][new_danger] = True
                    queue.append((nr, nc, steps + 1, new_danger))

    return -1


def main():
    R, C, F = map(int, input().split())
    S_row, S_col = map(int, input().split())
    T_row, T_col = map(int, input().split())


    start = (S_row - 1, S_col - 1)
    target = (T_row - 1, T_col - 1)

    
    grid = [list(map(int, input().split())) for _ in range(R)]

    result = rescue_vehicle(grid, R, C, F, start, target)

    if result != -1:
        print(result)
    else:
        print("Cesta neexistuje")


if __name__ == "__main__":
    main()
