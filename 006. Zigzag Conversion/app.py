class Solution:
    def print_2d_array(self, array):
        if not array:
            print()
            return

        def format_row(row):
            cells = [" " if not item else str(item) for item in row]
            return "|" + "|".join(cells) + "|"

        width = len(format_row(array[0]))
        print("_" * width)
        for row in array:
            print(format_row(row))
        print("_" * width)
        print()

    def calculate_zz_len(self, s_len, numRows):
        zz_len = 0
        remaining = s_len
        diag_len = numRows - 2
        while remaining:
            if remaining >= numRows:
                remaining -= numRows
                zz_len+=1
                if remaining >= diag_len:
                    remaining -= diag_len
                    zz_len += diag_len
                else:
                    zz_len+=remaining
                    remaining = 0
                    break
            else:
                remaining = 0
                zz_len+=1
                break
        return zz_len

    def convert(self, s: str, numRows: int) -> str:
        s_len = len(s)
        if s_len <= numRows or numRows == 1:
            return s

        zz_len = self.calculate_zz_len(s_len, numRows)

        zz = [["" for _ in range(zz_len)] for _ in range(numRows)]
        last_row = 0
        direction = 0
        word = list(s[::-1])
        for column in range(zz_len):
            if direction == 0:
                for row in range(numRows):
                    if not word:
                        break
                    zz[row][column] = word.pop()
                    last_row = row
                direction = 1
            elif direction == 1:
                last_row -= 1
                zz[last_row][column] = word.pop()
                if last_row == 1:
                    direction = 0
            self.print_2d_array(zz)
        
        result = ""

        for x in range(numRows):
            result += ''.join(zz[x])
        
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.convert("ABCDE", 4))

        