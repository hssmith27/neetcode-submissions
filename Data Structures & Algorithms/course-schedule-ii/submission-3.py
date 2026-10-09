class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        outgoing = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            outgoing[prereq].append(course)
            indegrees[course] += 1

        ready = []

        for i in range(numCourses):
            if indegrees[i] == 0:
                ready.append(i)

        res = []

        while ready:
            course = ready.pop()
            res.append(course)
            for other in outgoing[course]:
                indegrees[other] -= 1
                if indegrees[other] == 0:
                    ready.append(other)

        return res if len(res) == numCourses else []