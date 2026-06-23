class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top+bot) // 2
            if matrix[row][0] > target: #lowest value in current row is too large
                bot = row - 1
            elif matrix[row][-1] < target: # largest value in our row is too low, need to go up
                top = row + 1
            else:
                break

        if not (top <= bot): # no valid row was found
            return False
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l+r) // 2
            if target > matrix[row][mid]: # target higher than mid value, move left ptr up
                l += 1
            elif target < matrix[row][mid]:
                r -= 1
            else:
                return True
        return False