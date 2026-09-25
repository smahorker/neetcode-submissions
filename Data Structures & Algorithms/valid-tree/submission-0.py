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

    '''