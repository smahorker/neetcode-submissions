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
A course having incoming degrees means it has pre reqs to be met, however once these indegrees are accounted for - it can be used to satisfy other courses pre reqs

Need to return any valid order

Create a mapping of preReqs : courses unlocked as well as maintaing an indegree array to see whether a course is ready to be used to satisfy requirements

Create a queue to process courses that have no indegrees, because these courses can be used to unlock other courses - essentially moving us closer to freeing up every course so
there are no restrictions, which is the end requirement to be able to take every class
- pop the value, then append the course into order - its safe to append here because we've validated it being an unlocked course by having no indegrees being the only way it can be in the queue
- Loop through all the neighbors of our current node, decrease their indegree by 1 to account for this pre req freeing up for them, check whether after this decrement any of them are full unlocked - in which case add them to the queue
-- we dont update the order here because we would end up only updating order when we decremented the indegree, however there are courese that start off with no pre req, so if we only appended things when we performed a decrement after examining unlocked courses, these initial courese would never be added to order

Check whether len(order) == number(courses), since there may be some courses that were unreachable, for example in a cycle 2 courses would have an indegree of 1 as they are reliant on each other, however since they never met their own requirements they were never added to order, so its an invalid solution
'''