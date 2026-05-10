class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        while num > 0:
            if (m:= int(num / 1000)) > 0:
                roman += "M" * m
                num %= 1000
            
            if (c := int(num / 100)) > 0:
                if c == 9:
                    roman += "CM"
                elif c >= 5:
                    roman += "D" + ("C" * (c - 5))
                elif c == 4:
                    roman += "CD"
                else:
                    roman += "C" * c
                num %= 100

            if (x := int(num/10))>0:
                if x == 9:
                    roman += "XC"
                elif x >= 5:
                    roman += "L" + ("X" * (x - 5))
                elif x == 4:
                    roman += "XL"
                else:
                    roman += "X" * x
                num %= 10
            
            if (i := int(num/1))>0:
                if i == 9:
                    roman += "IX"
                elif i >= 5:
                    roman += "V" + ("I" * (i - 5))
                elif i == 4:
                    roman += "IV"
                else:
                    roman += "I" * i
                break
        return roman
