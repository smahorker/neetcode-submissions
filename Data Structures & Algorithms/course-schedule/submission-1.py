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
'''