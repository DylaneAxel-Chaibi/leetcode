class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)) :
            if nums[i] > 0 :
                continue
            if i > 0 and nums[i] == nums[i - 1] :
                continue
            target = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r :
                s = nums[l] + nums[r]
                if s < target :
                    l += 1
                elif s > target :
                    r -= 1
                else :
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1] :
                        l += 1
        return res