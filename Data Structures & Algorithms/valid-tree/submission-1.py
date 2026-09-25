class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()


        def dfs(node, parent):
            visited.add(node)
            for neigh in graph[node]:
                if neigh == parent: # skip node we came since its validated + in set
                    continue
                if neigh in visited:
                    return False
                if not dfs(neigh, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        else:
            return len(visited) == n


    '''
    A tree has n-1 edges

    Create a graph that maps all the edges, since its undirected, need the adjaceny list to represent going both ways since you can go up or down - this will introduce the parent
    into the neighbor values, but we can traverse from any part of the tree this way

    Create a visited set to see the value's we've seen in our tree so far, for it to not be a tree there must be a cycle present, so if its a node we've already visited then its a cycle

    Create dfs helper func, add node we're on to visited, loop through all the current nodes neighbors
    - if its the parent just skip this iteration, which is bound to be one of the neighbors since its undirected tree
    - if the neighbor is in visited, then we're in a cycle because we've already seen it in an "earlier" part of the tree as we were traversing down
    - Recursively call the dfs on the neighbor with node as the parent, if this evaluates to False - which only happens if its in the visited set, then return False - this return False
    will short circuit the call stack and will propogate up and make it so the if not dfs(0, -1) condition is met

    call if not dfs(0, -1), start at node 0, we also provide it a parent of -1 since thats impossible and the root has no parent

    if the dfs finished with no issue, then we found no cycles, however we have to make sure we visited every node and that there weren't any disconnected nodes in the edge list, if
    there were then its an invalid tree, so if we visited every node, then len(visited) == n



    '''