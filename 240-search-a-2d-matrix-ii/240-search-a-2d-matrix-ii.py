class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j = -1
        for row in matrix:
            while j + len(row) and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False