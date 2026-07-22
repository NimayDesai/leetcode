# Last updated: 7/22/2026, 4:58:43 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            dif=target-nums[i]

            if dif in d:
                return [d[dif],i]

            d[nums[i]]=i
                


                