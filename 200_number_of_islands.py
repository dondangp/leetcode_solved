from collections import deque
from typing import List

class Solutions:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        if not grid:
            return 0
        rows,cols = len(grid), len(grid[0])
        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = '0'

            while queue:
                x,y = queue.popleft()
                # explore all four directions
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx,ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        queue.append((nx,ny))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    numIslands+=1
                    bfs(r,c)
        return numIslands


# Create an instance of the class
sol = Solutions()

# input
grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]

print(sol.numIslands(grid))
