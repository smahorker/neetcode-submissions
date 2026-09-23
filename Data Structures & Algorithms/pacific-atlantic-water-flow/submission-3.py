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
Work outwards in, rather than dfs inward out since then we would need to check every cell which would be inefficient, we can already verify what works since anything on the edge meets an ocean so we start from the ocean edge and check adjacent nodes, its only a valid check if the adjacent node is greater than the one prior to it so that the water can flow down 
- the water does not need to go straight down, it can zigzag, obviously only in the 4 directions provided

Dfs function adds the current node to the related set, this way we the same node can be used to travel to different oceans, we don't need to worry about the node not being reachable again since the entire dfs exploration will cover all possible paths from that starting node, so any subpaths in a larger stream will be accounted for deeper in the call stack

1. check whether we are in bounds, check whether the adjacent node is not in the set, and check whether the adjacent node is greater than the original node, if it is that means we found a new valid path - we check that its not in the set because we dont want to get into an inifinite recursive loop and prevent repeat work - it the path we are moving to would have already been discovered if its in the set in a previous dfs
1.5. Once we found a valid node that is greater than the original, then dfs on that so we can go deeper, until the condition is no longer true the function returns on its own to one level higher in the call stack

In our for loop, say we start from the top left edge, then go right, and fully recurse down that path and eventually exit back into the original call in the bottom section of the code, when we call that next col value, even though we check all 4 directions we do nothing with it because it has already been visited inside of the set

return the list of nodes that in both the pacific and atlantic sets

Start from top, bot, left, or right edge and work inward based on if orig < new node, then add to set to prevent duplication and recursively call on it, check all 4 directions to see if it meets valid conditions to traverse deeper, once base case met across call stack return to original for loop call and move to next value in edge and continue until edge is exhausted - using 2 sets since there are 2 areas to flow to, if we only managed 1 set, it would isolate nodes to flow into only one ocean
'''