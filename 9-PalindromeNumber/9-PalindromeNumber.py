# Last updated: 7/22/2026, 4:58:40 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if list(str(x))[::-1] == list(str(x)):
            return True
        return False