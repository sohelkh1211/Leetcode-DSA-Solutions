# Lets consider example :- nums = [1,2,3,4]

# 1. Sort the given array.
# E.g :- nums = [1,2,3,4]

# 2. Pair adjacent elements because size of given array is even.
# E.g :- pairs :- (1,2), (3,4)

# 3. Compute sum of minimum of pair while pairing elements.
# E.g :- 
# max_sum = 0 
# In each iteration :- 
#    max_sum += min(pair) 

# 4. return max_sum

# https://leetcode.com/problems/array-partition/description/

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        max_sum = 0
        for i in range(0,len(nums)-1,2):
            max_sum += min(nums[i], nums[i+1])
        return max_sum