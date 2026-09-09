class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        raws = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)

        for i in range(9) :
            for j in range(9) :
                if board[i][j] == "." :
                    continue
                if (board[i][j] in cols[j]) or (board[i][j] in raws[i]) or (board[i][j] in sqrs[(i//3, j//3)]) :
                    return False
                cols[j].add(board[i][j])
                raws[i].add(board[i][j])
                sqrs[(i//3, j//3)].add(board[i][j])
        
        return True
        