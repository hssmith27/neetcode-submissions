class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        outgoing = [[] for _ in range(numCourses)]

        for course, req in prerequisites:
            outgoing[req].append(course)
            indegrees[course] += 1

        zeros = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                zeros.append(i)

        while zeros:
            course = zeros.pop()
 
            for other in outgoing[course]:
                indegrees[other] -= 1
                if indegrees[other] == 0:
                    zeros.append(other)

        return sum(indegrees) == 0
