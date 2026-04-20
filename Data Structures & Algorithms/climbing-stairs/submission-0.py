class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        for k in range(n//2 + 1) :
            res += math.comb(n-k, k)
        return res