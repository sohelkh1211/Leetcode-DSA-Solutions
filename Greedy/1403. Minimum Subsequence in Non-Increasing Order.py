# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/description/

from typing import List
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        elif len(nums) == 2:
            if nums[0] == nums[1]:
                return nums
            return [nums[nums.index(max(nums))]]

        nums.sort(reverse = True)
        subsequence_sum = 0
        index = 0
        remaining_sum = sum(nums)
        required_sum = 0

        while required_sum + nums[index] <= remaining_sum - nums[index]:
            required_sum += nums[index]
            remaining_sum -= nums[index]
            index += 1

        return nums[:index+1]