class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        i, down = 0, False
        rows = [""] * numRows

        for char in s:
            rows[i] += char
            if i == 0:
                down = True 
            elif i == numRows - 1:
                down = False         
            i += 1 if down else -1
        return ''.join(rows)
            