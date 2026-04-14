class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixSum = [[0]* len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)) :
            preSum = 0
            for col in range(len(matrix[0])) :
                preSum += matrix[row][col]
                self.prefixSum[row][col] = preSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2 + 1) :
            if col1 > 0 :
                sum += self.prefixSum[row][col2] - self.prefixSum[row][col1 - 1]
            else :
                sum += self.prefixSum[row][col2]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)