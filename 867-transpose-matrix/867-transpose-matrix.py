class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R = len(matrix)
        C = len(matrix[0])
        
        transpose = []
        for c in range(C):
            newRow = []
            for r in range(R):
                newRow.append(matrix[r][c])
            transpose.append(newRow)
        return transpose
        
        
        