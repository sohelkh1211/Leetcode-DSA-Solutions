# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/


from typing import List
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # Sort the numbers to deal with negatives first
        nums.sort()
        
        # Negate as many negative numbers as we can
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        
        # If we still have negations left, we can either negate the smallest number
        # or leave it as is if we have an even number of negations remaining.
        if k > 0:
            nums.sort()  # Sort again to find the smallest number
            if k % 2 == 1:  # Only if there's an odd number of negations left
                nums[0] = -nums[0]  # Negate the smallest number
        
        return sum(nums)