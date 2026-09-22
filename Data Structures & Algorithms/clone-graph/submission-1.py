"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
             
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None

'''
Create a hashmap to map the orig : copy, that way we dont get stuck in a recursive cycle or need to worry about duplicates

Create helper function that assigns finds neighbors of the current node, if the
examined node is already in the map, then just return that clone since it already exists and we can just point back to it

If the node doesnt exist, we need to create a copy of the node and search all of its neighbors recursively, when we visit
the neighbors recursively, we will also visit their neighbors as we work our way down the call stack, we go as deep as possible
then call back up from the lowest level visiting the next lowest levels neighbor

Call the dfs on initial node, but if its null then return None

'''

