class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        y_max = len(matrix)
        x_max = len(matrix[0])
        x = 0
        y = 0
        direction = "r"
        result = []
        rotations = 0
        for _ in range(x_max * y_max):
            result.append(matrix[y][x])
            if direction == "r":
                if x < (x_max - 1 - rotations):
                    x += 1
                else:
                    direction = "d"
                    y += 1
            elif direction == "d":
                if y < (y_max - 1 - rotations):
                    y += 1
                else:
                    direction = "l"
                    x-=1
            elif direction == "l":
                if x > (0 + rotations):
                    x -= 1
                else:
                    direction = "u"
                    rotations += 1
                    y-=1
            elif direction == "u":
                if y > (0 + rotations):
                    y -= 1
                else:
                    direction = "r"
                    x+=1
        return result
