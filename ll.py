import collections

def bfs(grid, start):
    wall, clear, goal = "#", ".", "*"
    size = 8
    queue = collections.deque([[start]])
    seen = set([start])
    while True:
        #print(queue)
        #print("konec queue")
        path = queue.popleft()
        #print(path)
        #print("\n")
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x+1,y-1), (x-1,y), (x-1,y+1), (x-1,y-1), (x,y+1), (x,y-1), (x+1,y+1)):
            if 0 <= x2 < size and 0 <= y2 < size and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


#musíme indexovat [y][x], jelikož nejdřív vybířáme řádek [y] a až poté index [x]
grid = ["........",
        "........",
        "........",
        "........",
        "....#...",
        "..###...",
        "..#*#...",
        "..#....."]

print(grid[5][4])

if bfs(grid, (5, 2)):
    print(bfs(grid, (5, 2)))
else: print(1)


