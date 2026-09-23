class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh+= 1
        
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (nr in range(len(grid)) and (nc in range(len(grid[0]))) and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            
            time += 1
        
        return time if fresh == 0 else -1

'''
Create a row and col var to track the grid, create a queue for bfs, keep track of time and fresh fruit

Loop through and identify which fruit are rotten so we can use multi source bfs, if it is rotten add it to
the queue to be processed, if it is fresh, then increment so we track it


'''