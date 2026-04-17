class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        res = []
        count = 0
        nums.sort()
        for i in range(1, len(nums)) :
            if nums[i] == nums[i - 1] :
                count += 1
            else :
                if count >= n :
                    res.append(nums[i-1])
                count = 0
        if count >= n :
            res.append(nums[-1])
        return res