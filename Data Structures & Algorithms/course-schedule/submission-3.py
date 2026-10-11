class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        outgoing = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            indegrees[course] += 1
            outgoing[prereq].append(course)

        available = []

        for i in range(numCourses):
            if indegrees[i] == 0:
                available.append(i)

        while available:
            course = available.pop()
            for out in outgoing[course]:
                indegrees[out] -= 1
                if indegrees[out] == 0:
                    available.append(out)

        return sum(indegrees) == 0
