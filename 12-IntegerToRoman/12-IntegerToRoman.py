# Last updated: 7/22/2026, 4:58:39 PM
class Solution:
    def intToRoman(self, num: int) -> str:
        str = ""
        while num > 0:
            if num >= 1000:
                num -= 1000
                str += "M"
            elif num >= 900:
                num -= 900
                str += "CM"
            elif num >= 500:
                num -= 500
                str += "D"
            elif num >= 400:
                num -= 400
                str += "CD"
            elif num >= 100:
                num -= 100
                str += "C"
            elif num >= 90:
                num -= 90
                str += "XC"
            elif num >= 50:
                num -= 50
                str += "L"
            elif num >= 40:
                num -=40
                str += "XL"
            elif num >= 10:
                num -= 10
                str += "X"
            elif num >= 9:
                num -= 9
                str += "IX"
            elif num >= 5:
                str += "V"
                num -= 5
            elif num >= 4:
                num -= 4
                str += "IV"
            elif num >= 1:
                num -= 1
                str += "I"
        return str