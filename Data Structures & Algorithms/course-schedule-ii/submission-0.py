class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inDegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDegree[course] += 1
        
        
        q = deque()
        for c in range(numCourses):
            if inDegree[c] == 0:
                q.append(c)
        
        order = []

        while q:
            curr = q.popleft()
            order.append(curr)

            for nxt in graph[curr]:
                inDegree[nxt] -= 1
                if inDegree[nxt] == 0:
                    q.append(nxt)
        
        return order if len(order) == numCourses else []

'''

'''