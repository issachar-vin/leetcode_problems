class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        ans = 0
        is_negative = True if x < 0 else False
        x = abs(x)
        while x != 0:
            digit = x % 10
            ans = ans * 10 + digit
            x //= 10
            if ans > MAX:
                return 0
        if is_negative:
            ans *= -1
        return ans