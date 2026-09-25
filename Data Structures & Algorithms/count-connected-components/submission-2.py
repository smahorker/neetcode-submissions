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
                size[rootY] += size[rootX]
            else:
                parent[rootY] = rootX
                size[rootX] = size[rootY]
            return True
        
        for a, b in edges:
            if union(a, b):
                count -= 1
        
        return count

'''
Create an initial list, going from 0 to n-1, each of these nodes represent their own root - in the initial state they are their own distinct trees, only when getting more information about their edges does this list adjust in accordance

Track the size of each of the roots, this way when we combine, we prefer the longest tree - this is the most ideal because if you attach a shorter tree to a root, then the height will
not increase as there exists another path that is longer coming out of the root, however if you combine a tree that is the same height, then the height increases by h + 1, since you're
essentially adding a new root to the tree you are combining
- This is superior to choosing the shorter tree, because in every case when you union the height will increase h+1 of the longer tree

Track the count, this is the count of seperate connected components, everytime we union, we combine 2 components and end up with 1
- this also supports isoalted components, say n = 5 edges = [[0,1]], the count would be 4 since only 1 union would happen, however we can't just do n - len(edges) because there may be edge cases like rootX = rootY where we try to combine 2 components with the same root which is impossible as they are already connected

Find - find the node x's root

- Recursively use current node's parent to locate the root, while at the same time updating the current node to match its parent to move faster up the tree on future calls

- lets say we call find(4), in the initial defintion of the array parent[4] should map to the value 4, but if the parent array has been updated, then it maps to a new root now, however
this root may still be a sub path of a larger tree - so in order to reduce operations in future looks ups, we compress the path to prefer the highest root, as unless there is a union to an equal or larger tree, this root will never change - however when this root does change our compression is no longer valid and needs to be propogated in a future call

-- find(4) calls its most recent root it was assigned to until it hits the true root of its component, and since parent[x] == x - essentially meaning the parent is in its original position, which confirms it as its own component, once the condition is no longer met, we return this value - which propogates down the entire callstack and assigns parent[x] = find(parent[x]) to be what we returned for every single call in the call stack


Union - combine the root of 2 trees

Find the root nodes of both of what we're unionizing, this is because even if the nodes we are trying to unionize are deep in their own components, we still need connect them by the root as the root is only way to verify whether both components have been connected yet, lets say we have 0-1-2-3 with 3 being the root and we call union(0, 2) if we didnt check their roots, then we would see that x != y, so we would proceed however they were already connected - so we must attach via the root to ensure they are seperate components

If you're worried you'll find the same numbers on your way traversing up to find the root, thats a non issue as if you were to run into 0 and 2 for example on different sub paths, they would both eventually lead to the same root if they were in the same component as you went up the levels

Check the sizes of each tree, assign the smaller tree to the root of the larger tree in accordance to which root is larger, then udpate the size accordingly

return True after this point because its a valid union, we need a boolean because in an invalid union we dont want to update the count as no merge happened, so the number of seperate components stayed the same

Call the union function on (a, b) in our list of edges in order to build up our trees, if a union was successful that means 2 seperate components merged, so decrement the count by 1

We are not building a perfect representation of edge list, we may attach a subpath to a root that was supposed edge list input had it assigned to node in a different path, but we assign to the root for optimal height distribution, however since the graph is undirected connected, these nodes are still reachable to one another, the edge list doesnt necessarily mean one edge has to have a direct edge to the other, they just have to exist in one part of the same component
'''