def bfs_and_closed(start, target):
    queue = [start]
    closed_list = set()
    closed_list.add(start)
    steps = 0

    while queue:
        current = queue.pop(0)

        if current == target:
            return steps

        for next_num in [current + 1, current - 1]:
            if next_num not in closed_list:
                queue.append(next_num)
                closed_list.add(next_num)

        steps += 1

    return -1


start = 1
target = 100
result = bfs_and_closed(start, target)
if result != -1:
    print(f"Target {target} found in {result} steps.")
else:
    print(f"Target {target} is not reachable from {start}.")
