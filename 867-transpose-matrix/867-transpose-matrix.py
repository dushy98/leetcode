class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # made the 1-liner more readable
        return [[matrix[i][j] 
                    for i in range(len(matrix))] 
                        for j in range(len(matrix[0]))]

        
        
        