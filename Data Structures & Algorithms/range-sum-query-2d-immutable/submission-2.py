class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixSum = [[0]* len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)) :
            preSum = 0
            for col in range(len(matrix[0])) :
                preSum += matrix[row][col]
                if row > 0 :
                    self.prefixSum[row][col] = preSum + self.prefixSum[row-1][col]
                else :
                    self.prefixSum[row][col] = preSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > 0 and col1 > 0 :
            return self.prefixSum[row2][col2] - self.prefixSum[row2][col1 - 1] - self.prefixSum[row1 - 1][col2] + self.prefixSum[row1 - 1][col1 - 1]
        elif row1 == 0 and col1 > 0 :
            return self.prefixSum[row2][col2] - self.prefixSum[row2][col1 - 1]
        elif row1 > 0 and col1 == 0 :
            return self.prefixSum[row2][col2] - self.prefixSum[row1 - 1][col2] 
        else :
            return self.prefixSum[row2][col2]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)