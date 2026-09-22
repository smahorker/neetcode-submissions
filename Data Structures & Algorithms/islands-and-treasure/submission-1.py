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
Define row, col, visited set, and the queue

addRoom checks whether up, down, left, or right is a valid move, if it isnt then return, otherwise we need to explore the empty
room, so add it to the queue to be processed on the next level and mark it as visited, future calls dont infinitely queue on it

Find all the gates as these are our starting point, we are doing a multi source bfs, so we move 1 out from each gate on every
iteration, this way when they finally collide, since the first gate to reach a room is the closer one, it will be marked properly

Go through the entire level in the queue, using range(len(q)) since range q doesnt work since you cant internpret the q as an int
1. pop the leftmost value since its the first value that entered the queue, dist tracks the distance at our current level, only
once all the values in our current queue depth have been processed will the distance go up - setting len(q) allowed us ensure
we process one level at a time

2. Go up, down, left, and right, since this is an adjacent node, its 1 level deeper, so we dont update the dist here - these nodes will be accounted for in the queues next level

3. Once we've processed all the nodes in the entire level, then we move onto processing the adjacent nodes and checking whether they have any adjacent nodes themselves, only when the queue is empty does that mean we  hit the base case for addRoom on every
check, so we can exit the code

4. dist gets incremented on the last level a final time, but it doesnt matter since we dont return it
'''