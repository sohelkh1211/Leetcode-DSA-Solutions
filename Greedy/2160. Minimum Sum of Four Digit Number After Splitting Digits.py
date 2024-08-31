class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(str(num),reverse=True)  
        res = 0
        for i in range(4):
            if i <= 1:
                res += int(num[i])*(10**0)
            else:
                res += int(num[i])*(10**1)
        return res

s = Solution()
num = 2932
ans = s.minimumSum(num)
print(ans)

# Javascript
'''var minimumSum = function(num) {
    num = num.toString().split("");
    num.sort((a,b) => b-a);
    let res = 0;
    num.forEach((n, index) => {
        if(index <= 1) {
            res += parseInt(n)*10**0;
        } else {
            res += parseInt(n)*10;
        }
    })
    return res;
};

var num = 2932;
console.log(minimumSum(num));
'''

