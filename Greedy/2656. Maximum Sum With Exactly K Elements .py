# https://tinyurl.com/yyuuxbm2
class Solution:
    def maximizeSum(self, nums, k):
        max_num = max(nums)
        score = max_num

        for _ in range(1, k):
            max_num += 1
            score += max_num
        return score

# Java
'''class Solution {
    public int maximizeSum(int[] nums, int k) {
        int max_num = Arrays.stream(nums).max().getAsInt();
        int score = max_num;

        for(int i = 1; i < k; i++) {
            max_num += 1;
            score += max_num;
        }

        return score;
    }
}'''

# JavaScript
'''
var maximizeSum = function(nums, k) {
    let max_num = Math.max(...nums);
    let score = max_num;

    for(let i = 1; i < k; i++) {
        max_num += 1;
        score += max_num;
    }
    return score;

};
'''