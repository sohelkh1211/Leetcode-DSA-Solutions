# https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        s = list(s)

        while start <= end:
            if s[start] != s[end]:
                new_s = s
                new_s.pop(end)
                if new_s != new_s[::-1]:
                    return 0
                new_s1 = s
                new_s1.pop(start)
                if new_s1 != new_s1[::-1]:
                    return 0
            start += 1
            end -= 1
        
        return 1