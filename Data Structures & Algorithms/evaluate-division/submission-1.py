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
Graph maps node : {neighbor : value, neighbor : value, ...} - so if it takes the path to this neighbor, thats the weightage of the path

Assign values to each edge toward a neighbor, graph[a][b] = val means for node a, going to its neighbor b will accumulate that value by taking that path

Dfs function - takes x, y, set of visited nodes in this path

- a new set is tracked for each unique path we take, dont need to worry about spillover between different paths in the call stack

Check base of arriving at our destination, if so then we return 1, which effectively applies the current weight by itself since we're the final node

Mark the node as visited so we don't revisit this same path on the next dfs call

Loop through all of the current nodes neighbors so we are able to take all available paths until exhausted

- if the neighbor exists in the set, then dont take that path as we've already explored it - if a path is explored and didn't end exit the dfs by hitting the base case, then its a non valid path as we exit as soon as we see a valid route and we go as deep as possible in a route as we can

- Continue calling dfs until we go as deep as possible, at this point there are no neighbors for us to take due to the node not having any or the neighbors left have already been visited, so we can start working our way backwards 
-- if we hit our target dst we would immediately return 1 and would not recurse down its neighbors excessively, however if we did not hit our target we would return -1 which would propogate up the call stack for that path as we marked every node in this path as visited, but if we move back 1 step in the call stack and there are still other dfs calls to be made - these would execute as intended and verify themselves

Only when we found a valid path, do we start calculating backwards from the destination - weight * sub

Create a results array, if the node doesnt exist in the graph, then append -1 to the result for this query, however this doesnt exclude unreachable nodes - if a node was isolated with no neighbors reaching it, we would still perform the dfs search looking for it, we would traverse every single possible neighbor reachable from source, but not the entire graph

Otherwise call the dfs on it, passing in x, y, and a fresh set for every call recursive call
'''