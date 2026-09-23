class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        row, col = len(board), len(board[0])

        def mark(r, c):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                if r < 0 or r == row or c < 0 or c == col or board[r][c] != 'O':
                    continue
                board[r][c] = 'S'
                stack.append((r+1, c))
                stack.append((r-1, c))
                stack.append((r, c+1))
                stack.append((r, c-1))

        # Scan every column, going down row by row until the last row on the left and right edge
        for r in range(row):
            mark(r, 0) # start at left corner, row 0, col 0
            mark(r, col-1) # right corner, row 0, last col
        # this loop ascends downward
        for c in range(col):
            mark(0, c) # left corner, row 0 col 0
            mark(row-1, c) # bottom right corner, last row, col 0
        # this loop traverses horizontally

        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'S':
                    board[r][c] = 'O'

