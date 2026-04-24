class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(i, j, visited) :
            if (i,j) in visited :
                return 0
            if not(0 <= i < len(grid) and 0 <= j < len(grid[0])) or  grid[i][j] == 0:
                return 1
            visited.add((i,j))
            return dfs(i + 1, j, visited) +  dfs(i - 1, j, visited) +  dfs(i, j + 1, visited) +  dfs(i, j - 1, visited)

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 1 :
                    return dfs(i, j, visited)