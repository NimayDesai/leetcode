# Last updated: 7/22/2026, 4:58:42 PM
import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        return statistics.median(nums1)