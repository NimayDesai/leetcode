# Last updated: 7/22/2026, 4:58:27 PM
import statistics

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return statistics.mode(nums)