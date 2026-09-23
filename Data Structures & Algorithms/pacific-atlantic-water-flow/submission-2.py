class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in [(1,0), (-1, 0), (0,1),(0, -1)]:
                nr, nc = r + dr, c + dc
                if nr in range(row) and nc in range(col) and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        for c in range(col):
            dfs(0, c, pacific)
            dfs(row-1, c, atlantic)
        for r in range(row):
            dfs(r, 0, pacific)
            dfs(r, col-1, atlantic)
        
        return[list(cell) for cell in pacific & atlantic]

'''
Work outwards in, rather than dfs inward out, because then we would have to explore every path and it would be hard
'''