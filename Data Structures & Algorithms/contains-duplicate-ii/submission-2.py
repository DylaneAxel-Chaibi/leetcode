class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0 or len(nums) < 2:
            return False
        l, r = 0, min(len(nums) - 1, k)
        while r < len(nums) :
            if nums[l] == nums[r] :
                return True
            r -= 1
            if r == l :
                l += 1
                r = k + l
        return False