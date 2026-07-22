# Last updated: 7/22/2026, 4:58:38 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i, char in enumerate(s):
            if i == len(s) - 1:
                total += mapping[char]
                break

            if char == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                total -= 1
            elif char == 'X' and (s[i + 1] == 'C' or s[i + 1] == 'L'):
                total -= 10
            elif char == 'C' and (s[i + 1] == 'M' or s[i + 1] == 'D'):
                total -= 100
            else:
                total += mapping[char]
        return total