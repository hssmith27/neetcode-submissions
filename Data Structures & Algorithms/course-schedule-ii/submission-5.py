class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        outgoing = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            indegrees[course] += 1
            outgoing[prereq].append(course)

        available = []

        for i in range(numCourses):
            if indegrees[i] == 0:
                available.append(i)

        res = []

        while available:
            course = available.pop()
            res.append(course)
            for out in outgoing[course]:
                indegrees[out] -= 1
                if indegrees[out] == 0:
                    available.append(out)

        return res if len(res) == numCourses else []
