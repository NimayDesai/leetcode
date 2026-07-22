# Last updated: 7/22/2026, 4:58:34 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        L = 0
        R = len(height)-1
        maxR = height[-1]
        total = 0    
        while L < R:
            if maxR > maxL:
                L += 1
                total += max(maxL - height[L], 0)
                maxL = max(maxL, height[L])
            else:
                R -= 1
                total += max(maxR - height[R], 0)
                maxR = max(maxR, height[R])
        return total

