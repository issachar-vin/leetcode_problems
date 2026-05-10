from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        n = len(grid)
        m = len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[y][x] != "1":
                return
            grid[y][x] = "0"
            dfs(x, y - 1)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x + 1, y)

        for y in range(n):
            for x in range(m):
                if grid[y][x] == "1":
                    islands += 1
                    dfs(x, y)

        return islands