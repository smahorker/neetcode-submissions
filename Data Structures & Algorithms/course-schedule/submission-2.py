class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visiting = set() # current dfs path
        done = set() # fully explored

        def hasCycle(node):
            if node in visiting:
                return True
            if node in done:
                return False
            
            visiting.add(node)
            for neighbor in graph[node]:
                if hasCycle(neighbor):
                    return True
            visiting.remove(node)
            done.add(node)
            return False
        
        for course in range(numCourses):
            if hasCycle(course):
                return False
        return True



'''
If course A needs course B and course B needs course A, then its impossible -detecting a cycle

Store the courses pre req in an adjacency list, key - pre req, value - courses that depend pre reqs, pre reqs -> dependents in graph
- what does finishing course X unlock for us to take, then traverse down those courses
to see if there is a cycle back to a pre req, since if there is a cycle back to a 

[[1,0],[2,1],[3,2],[1,3]]

Must take course 0 before course 1

Take course 0->1->2->3->1

Must take course 1 in order to transitively take course 3, but also must take course 3
in order to take course 1

If course is a pre req for its own pre reqs, its a cycle

1. Create mapping of pre req : unlocks, this adjaceny list builds a list because one pre req might unlock multiple courses, so its not a 1:1 mapping

2. Create visiting set to track current dfs iteration and done set to prune traversed paths - we would have traversed down a path fully in a previous iteration because of dfs, so once a node is visited once, it doesnt need to be visisted again

3. Helper function that detects cycle, check whether the node is in visited, if so then it is a cycle because the current dfs path has seen it before - this means the course we are unlocking was a pre req for other courses earlier in the call stack, so its a cycle

3.1. Check whether the node is in the done set, so we can skip over redundant searches

3.2. If we passed these, then its a new node, so add it to the visiting set as its on the current dfs path, then traverse its neighbors to go as deep as possible - the neighbors are the nodes its adjacent to - go as deep as possible where we will check the base cases to verify a cycle

3.3. Once you have fully traversed this entire path's neighbors and the last node has no neighbors, we've verified it as a non cycle, so we can remove the current node from visiting and add it to done, as we've verified this far in the path there can't be any cycles

3.4. We may have verified this subpath, but coming from the root of our callstack, as we unwind the call stack, a different sub path may be a cycle - which will be discovered as the dfs unwinds

3.5. Once we've verified all the nodes and ensure they hit the appropriate base cases, we default to False as no node was in the visiting set

4. Loop through each number in range(numCourses), the range of courses go from 0 to numCourses-1, and we access the relevant adjacency list via index as well, if we've already validated the course we pass via this loop, then the base case of if node in done will trigger and we will move onto the next call
'''