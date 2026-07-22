# Last updated: 7/22/2026, 4:58:42 PM
class Solution:
    def check_idx(self, s: str, idx: int) -> int:
        """Starts at idx and counts unique characters until a repeat is found."""
        seen = set()
        count = 0
        for i in range(idx, len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                count += 1
            else:
                # Stop as soon as we hit a duplicate
                break
        return count

    def lengthOfLongestSubstring(self, s: str) -> int:
        highest = 0
        
        # Check every possible starting point
        for i in range(len(s)):
            # From this index, how many unique characters follow?
            current_streak = self.check_idx(s, i)
            
            # Update the record if this streak is longer
            if current_streak > highest:
                highest = current_streak
                
        return highest