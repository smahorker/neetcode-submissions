class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for dr, dc in [(-1, 0), (1,0), (0,1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] == 0:
                            perimeter += 1
        return perimeter

'''
rows are the total number of lists in our matrix, as those are stacked

cols are the vertical columns, which is decided by the amount of elements in a single list since all lists are equal size

Loop through each list in mtx, so you need 2 for loops, one for the current row, then another going through each value in
the columns - select a row and walk through columns(idx)

If grid[r][c] == 1, that means you are visiting a valid block, so you want to check if its an internal piece, or there is
water surrounding it, only if its an edge or water surrounding it can be permiter, since an internal piece is the area

Loop through a tuple that shifts the r and c value up, down, left, right - this checks all directions by accessing


'''

