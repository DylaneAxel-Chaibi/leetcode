class Solution:
    def sumOfSqrs(self, n: int) -> int:
        res = 0
        while n > 0 :
            res = res + (n % 10)**2
            n = n // 10
        return res

    def isHappy(self, n: int) -> bool:
        seen = set()
        while self.sumOfSqrs(n) != 1 :
            if n in seen :
                return False
            seen.add(n)
            n = self.sumOfSqrs(n)
        return True