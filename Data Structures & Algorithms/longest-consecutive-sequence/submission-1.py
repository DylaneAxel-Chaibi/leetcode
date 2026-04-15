class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        res = 0
        sorted_nums = sorted(nums)
        curr = sorted_nums[0]
        streak = 1
        for i, num in enumerate(sorted_nums) :
            if num == curr :
                continue
            elif num == 1 + curr :
                streak += 1
                curr = num
                # print(streak)
            else :
                res = max(res, streak)
                print(streak)
                curr = num
                streak = 1
        res = max(res, streak)
        return res