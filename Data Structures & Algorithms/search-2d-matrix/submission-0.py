class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        for m in range(len(matrix) - 1, -1, -1):
            if matrix[m][0] <= target:
                row = m
                break
                
        low = 0
        high = len(matrix[row])

        while low < high:
            mid = low + (high - low) // 2
            if matrix[row][mid] >= target:
                high = mid
            elif matrix[row][mid] < target:
                low = mid + 1

        return True if (low < len(matrix[row]) and matrix[row][low] == target) else False