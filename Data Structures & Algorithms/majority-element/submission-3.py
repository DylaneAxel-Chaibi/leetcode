class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bit = [0] * 32
        result = 0
        for num in nums :
            for i in range(32) :
                bit[i] += ((num >> i) & 1)
        for i,b in enumerate(bit) :
            if b > len(nums)/2 : 
                result += 2**i
        return result
