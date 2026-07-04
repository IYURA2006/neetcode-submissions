class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows = len(matrix)
        cols = len(matrix[0])
        

        for j in range(rows):
            for i in range(cols):

                
                cur_sum = 0
                #if top border
                if j != 0:
                    cur_sum += matrix[j-1][i]

        
                #if left border
                if i != 0:
                    cur_sum += matrix[j][i-1]

                if i != 0 and j != 0:
                    cur_sum -= matrix[j-1][i-1]

                cur_sum += matrix[j][i]
                matrix[j][i] = cur_sum
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        res += self.matrix[row2][col2]
        #top border
        if row1 != 0:
            res -= self.matrix[row1-1][col2]
            print(res)

        #left border
        if col1 != 0:
            res -= self.matrix[row2][col1-1]
            print(res)
        
        if col1 != 0 and row1 != 0:
            res += self.matrix[row1-1][col1-1]


        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)