class Solution:
    def totalNQueens(self, n: int) -> int:
        diagonal_1 = set()
        diagonal_2 = set()
        usedColumns = set()
        
        return self.helper(n, diagonal_1, diagonal_2, usedColumns, 0)
        
    #helper function to modularize
    def helper(self, n, diagonal_1, diagonal_2, usedColumns, row):
        if row == n:
            return 1
        
        solutions = 0
        
        for column in range(n):
            if row + column in diagonal_1 or row - column in diagonal_2 or column in usedColumns:
                continue
                
            diagonal_1.add(row + column)
            diagonal_2.add(row - column)
            usedColumns.add(column)
            
            solutions += self.helper(n, diagonal_1, diagonal_2, usedColumns, row + 1)
            
            diagonal_1.remove(row + column)
            diagonal_2.remove(row - column)
            usedColumns.remove(column)
        
        return solutions
            
            
            
        