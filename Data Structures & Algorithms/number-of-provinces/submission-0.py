class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(cities, city, visited) :
            visited.add(city)
            for c in range(len(cities[city])) :
                if cities[city][c] == 1 and c not in visited :
                    dfs(cities, c, visited)
        visited = set()
        count = 0
        for city in range(len(isConnected)) :
            print(visited)
            if city not in visited :
                dfs(isConnected, city, visited)
                count += 1
        return count