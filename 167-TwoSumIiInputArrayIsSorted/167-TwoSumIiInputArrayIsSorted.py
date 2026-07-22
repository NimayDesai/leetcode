# Last updated: 7/22/2026, 4:58:28 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        so = sorted(numbers)

        a = 0
        b = len(so) - 1

        while True:
            tot = so[a] + so[b]
            if tot == target:
                return [a + 1, b + 1]
            
            if tot > target:
                b -= 1
            if tot <= target:
                a += 1
            
