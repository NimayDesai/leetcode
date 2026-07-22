# Last updated: 7/22/2026, 5:07:15 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        idx = 0
4        minl = min(len(word1), len(word2))
5        a = True if len(word1) > len(word2) else False
6        res = ""
7        while idx < minl:
8            res += word1[idx] + word2[idx]
9            idx += 1
10        res += word1[idx:] if a else word2[idx:]
11        return res
12        