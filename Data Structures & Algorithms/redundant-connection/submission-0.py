class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        size = [1] * (n+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False # cant union on itself, they have the same root
            if size[rootX] < size[rootY]:
                parent[rootX] = rootY
                size[rootY] += size[rootX] # dont need to update rootX size because when we call find on rootX now it will go to rootY which has the true state of the entire tree
            else:
                parent[rootY] = rootX
                size[rootX] += size[rootY]
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
    