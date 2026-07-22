# Last updated: 7/22/2026, 4:58:26 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cons = 0
        for i in nums:
            if i == 1:
                cons += 1
            else:
                cons = 0
            
            res = max(cons, res)
        return res