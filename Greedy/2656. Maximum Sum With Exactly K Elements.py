# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

from typing import List
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        ans = [max_num]
        for _ in range(k-1):
            ans.append(ans[-1]+1)
        return sum(ans)

S1 = Solution()
nums = [1,2,3,4,5]
k = 3
ans = S1.maximizeSum(nums, k)
print(ans)

# Greedy approach

# First, Find maximum number max_num in the array nums. E.g: max_num = max(nums) max_num = 5
# Initialize ans array with first element as max_num. E.g: ans = [5]
# Iterate upto k-1 using for loop add the element to the ans array which is one more than last element in the array i.e ans[-1] + 1.
# E.g :- k = 0
# ans = [5,6] Appended element = 5+1
# E.g :- k = 1
# ans = [5,6,7] Appended element = 6+1