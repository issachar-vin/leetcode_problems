class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31
        is_negative = True if x<0 else False
        if is_negative:
            x*=-1
        try:
            x = int(str(x)[::-1])
        except:
            return 0
        if x > MAX:
            return 0
        if is_negative:
            x *= -1
        return x