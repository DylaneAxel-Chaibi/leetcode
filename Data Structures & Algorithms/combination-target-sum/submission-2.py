class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, currList, total) :
            if total == target :
                res.append(currList[:])
                return
            if i >= len(nums) : 
                return
            if total > target :
                i = i + 1
                return 
            currList.append(nums[i])
            dfs(i, currList, total + nums[i])
            currList.remove(nums[i])
            dfs(i+1, currList, total)
        dfs(0, [], 0)
        return res
