class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(visited) :
            if len(visited) == len(nums) :
                res.append(visited[:])
                return
            for i in nums :
                if i not in visited :
                    visited.append(i)
                    dfs(visited)
                    visited.remove(i)
        dfs([])
        return res

        

