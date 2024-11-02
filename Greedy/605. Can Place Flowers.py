# https://leetcode.com/problems/can-place-flowers/description/

from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # This will count how many flowers can be placed
        i = 0
        
        while i < len(flowerbed):
            # Check if the current position is empty and the adjacent positions are also empty
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1  # Place a flower
                count += 1  # Increment the count of flowers placed
            
            i += 1  # Move to the next position
        
        return count >= n  # Check if we can place at least 'n' flowers