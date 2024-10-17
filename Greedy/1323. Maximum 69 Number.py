# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        for i in range(len(num)):
            if num[i] == "6":
                num[i] = "9"
                break
        num = "".join(map(str,num))
        return int(num)