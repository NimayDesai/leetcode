# Last updated: 7/22/2026, 4:58:23 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 0
        r = n
        a = []
        while r < len(nums):
            a.append(nums[l])
            a.append(nums[r])
            l += 1
            r += 1
        return a