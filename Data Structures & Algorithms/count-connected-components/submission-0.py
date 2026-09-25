class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        size = [1] * n
        count = n

        def find(x): # recurse on root and reassign nodes
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)

            if rootX == rootY:
                return False
            if size[rootX] < size[rootY]:
                parent[rootX] = rootY
                size[rootY] += rootX
            else:
                parent[rootY] = rootX
                size[rootX] = rootY
            return True
        
        for a, b in edges:
            if union(a, b):
                count -= 1
        
        return count

        
