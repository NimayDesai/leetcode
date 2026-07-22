# Last updated: 7/22/2026, 4:58:22 PM
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        tot = 0
        for i in str(n):
            tot += int(i)
        return tot