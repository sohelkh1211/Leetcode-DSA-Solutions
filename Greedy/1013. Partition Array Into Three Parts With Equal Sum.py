# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/

from typing import List
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        l, r, s = 1, len(arr) - 2, sum(arr)

        if s % 3 != 0:
            return 0
        
        lSum, rSum, average = arr[0], arr[-1], s // 3
        
        while l <= r:
            if l == r:
                return 0
            if l < r and lSum != average:
                lSum += arr[l]
                l += 1
            if l < r and rSum != average:
                rSum += arr[r]
                r -= 1
            if lSum == average == rSum:
                return 1
            