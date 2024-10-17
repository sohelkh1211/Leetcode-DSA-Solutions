# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

from typing import List
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        ans = 0
        seats.sort()
        students.sort()

        for i in range(len(seats)):
            ans += abs(seats[i]-students[i])
        
        return ans
    
S1 = Solution()
seats = [3,1,5]
students = [2,7,4]
ans = S1.minMovesToSeat(seats,students)
print(ans)