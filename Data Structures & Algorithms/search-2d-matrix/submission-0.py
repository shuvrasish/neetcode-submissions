class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        l, r = 0, len(matrix) * n - 1

        while l <= r:
            mid = l + (r - l) // 2
            # if mid is 6 and m = 3 and n = 4, row would be 2nd (index 1) and column will be 3rd (index 2)
            # mid % n = 2 (col); mid // n = 1 (row)
            row = mid // n
            col = mid % n

            el = matrix[row][col]

            if el > target:
                r = mid - 1
            elif el < target:
                l = mid + 1
            else:
                return True
            
        return False