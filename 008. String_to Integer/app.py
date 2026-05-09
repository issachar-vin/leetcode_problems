MAX = 2**31

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        is_negative = False
        number = 0
        for index, char in enumerate(s):
            if not char.isdigit():
                if index == 0 and char not in ["-", "+"]:
                    return 0
                elif index == 0 and char in ["-", "+"]:
                    is_negative = True if char == "-" else False
                else:
                    break
            else:
                number = number * 10 + int(char)
        if number > MAX:
            number = MAX - 1 if is_negative else MAX
        if is_negative:
            number *= -1 
        return number
