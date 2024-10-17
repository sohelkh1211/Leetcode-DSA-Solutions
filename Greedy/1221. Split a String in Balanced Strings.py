# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced_strings = 0
        r_count = 0
        s_count = 0
        for i in range(len(s)):
            if s[i] == "R":
                r_count += 1
            else:
                s_count += 1
            if r_count == s_count:
                r_count = s_count = 0
                balanced_strings += 1
            print(r_count, s_count)
        return balanced_strings

S1 = Solution()
s = "RLRRLLRLRL"
ans = S1.balancedStringSplit(s)
print(ans)