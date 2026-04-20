class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,i) :        
            if i == len(word) :
                return True
            if not(0 <= r < len(board) and 0 <= c < len(board[0])) or word[i] != board[r][c] :
                return False
            tmp = board[r][c]
            board[r][c] = '#'
            found = (dfs(r - 1, c, i + 1) or dfs(r + 1, c, i +1) or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1))
            board[r][c] = tmp
            return found
        for r in range(len(board)) :
            for c in range(len(board[0])) :
                if board[r][c] == word[0] :
                    if dfs(r, c, 0) :
                        return True
        return False

            