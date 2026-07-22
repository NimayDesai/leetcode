# Last updated: 7/22/2026, 4:58:40 PM
class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        if x < 0:
            neg = -1
        res = int(str(x*neg)[::-1])*neg
        if -2**31 <= res <= 2**31 - 1:
            return res
        else:
            return 0