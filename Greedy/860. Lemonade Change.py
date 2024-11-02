# https://leetcode.com/problems/lemonade-change/description/

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        available = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                available[5] += 1
            elif bill == 10:
                if available[5] >= 1:
                    available[5] -= 1
                    available[10] += 1
                else:
                    return False
            elif bill == 20:
                if available[10] >= 1 and available[5] >= 1:
                    available[5] -= 1
                    available[10] -= 1
                    available[20] += 1
                elif available[5] >= 3:
                    available[5] -= 3
                    available[20] += 1
                else:
                    return False
        return True