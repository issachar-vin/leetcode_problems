from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        MAX_X = len(mat[0])
        MAX_Y = len(mat)
        MAX = MAX_X * MAX_Y
        queue = deque([])
        for y in range(MAX_Y):
            for x in range(MAX_X):
                if mat[y][x] == 0:
                    queue.append((y,x))
                else:
                    mat[y][x] = MAX
        while queue:
            cur = queue.popleft()
            y = cur[0]
            x = cur[1]
            value = mat[y][x]

            # Up
            if y > 0 and mat[y-1][x] > value:
                mat[y-1][x] = value + 1
                queue.append((y-1,x))

            # Down
            if y < MAX_Y - 1 and mat[y+1][x] > value:
                mat[y+1][x] = value + 1
                queue.append((y+1,x))

            # Left
            if x > 0 and mat[y][x-1] > value:
                mat[y][x-1] = value + 1
                queue.append((y,x-1))

            # Right
            if x < MAX_X - 1 and mat[y][x+1] > value:
                mat[y][x+1] = value + 1
                queue.append((y,x+1))

        return mat    
        