# https://leetcode.com/problems/maximum-odd-binary-number/description/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # First, take the count of all ones in the given binary string
        count_of_1 = s.count('1')

        # If length of string is 1 or number of 1's is equal to length of string then return original string
        if len(s) == 1 or count_of_1 == len(s):
            return s
        
        # Add all the 1's except one 1 at the start of the ans string array and add all the zeros after this and finally add remaining one 1 at the end.
        ans = ['1']*(count_of_1-1)+['0']*(len(s)-count_of_1)+['1']
        return "".join(ans)

S1 = Solution()
s = "0101"
ans = S1.maximumOddBinaryNumber(s)
print(ans)