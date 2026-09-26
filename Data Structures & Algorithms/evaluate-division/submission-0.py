class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val
        
        def dfs(src, dst, visited):
            if src == dst:
                return 1.0
            visited.add(src)
            for neighbor, weight in graph[src].items():
                if neighbor in visited:
                    continue
                sub = dfs(neighbor, dst, visited)
                if sub != -1.0:
                    return weight * sub
            return -1.0

        results = []
        for x, y in queries:
            if x not in graph or y not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(x, y, set()))
        return results

'''

Graph maps node : {neighbor : value, neighbor : value, ...} - so if it takes the path to this neighbor, whats the weightage of the path
'''