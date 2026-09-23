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

Tracking fresh handles edge case of entering queue when only rotten fruit are available, causing us to increment the time by 1 even though all our grid checks returned false
- the same is true for why we have q and fresh, if we don't then in our final iteration when everything is rotten, we process the queue and find nothing to turn rotten, but we increment the timer which causes a +1 we dont want
-- cant just default to doing timer -1 and having this slip through due to single empty cell case

Collision is handled via checking grid[nr][nc] == '1', when we identify a fresh orange and turn it rotten, we
update it in the grid, this essentially marks it as visited and no other source will visit, instead they will
skip this direction and move onto a different one

while q and fresh, so when either are exhausted, loop through the current level of the queue, pop out the leftmost value in the q, loop through moving in all 4 directions, check whether that direction is in bounds and is fresh, if so update it to rotten and add that node to the queue so we can explore whether other fruit is next to it to get rotten, and decrement fresh since we made a fresh fruit rotten
- Only after the entire level is complete which means we went 1 level deeper for all our rotten sources, then we increment time since that means all sources of rotten fruit has gone 1 level further deep
'''