# Last updated: 7/22/2026, 4:58:37 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        pre2 = ""
        num = 1
        a = True
        while a:
            pre2 = strs[0][0:num]
            for i in strs:
                if i[0:num] != pre2 or not i or num > len(i):
                    a = False
                    break
            if a:
                pre = pre2
                num += 1
        return pre