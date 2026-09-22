class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r, c):
            if r < 0 or r == row or c < 0 or c == col or (r, c) in visit or grid[r][c] == -1:
                return 
            visit.add((r,c))
            q.append([r, c])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            dist += 1


'''
Go through the entire level in the queue, using range(len) 
'''