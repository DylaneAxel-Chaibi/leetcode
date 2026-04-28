class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, visited) :
            if len(visited) == k :
                res.append(visited[:])
                return
            for j in range(i, n+1) :
                visited.append(j)
                dfs(j + 1, visited)
                visited.pop()
        # 
        dfs(1, [])
        return res
