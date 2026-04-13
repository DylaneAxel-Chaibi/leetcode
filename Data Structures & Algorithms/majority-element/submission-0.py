class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums)
        for n in s :
            count = 0
            for num in nums :
                if n == num :
                    count += 1
            if count >= len(nums)/2 : return n
