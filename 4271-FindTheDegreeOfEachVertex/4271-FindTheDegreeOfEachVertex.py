# Last updated: 7/22/2026, 4:58:21 PM
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res = []
        for i in matrix:
            res.append(sum(i))
        return res
