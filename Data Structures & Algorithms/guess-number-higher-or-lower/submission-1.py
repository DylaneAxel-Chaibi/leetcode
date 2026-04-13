# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(n) == 0 : return n
        l = 1
        r = n
        while l <= r :
            x = (l + r) // 2
            if guess(x) == -1 :
                r = x
            elif guess(x) == 1 :
                l = x
            else : return x