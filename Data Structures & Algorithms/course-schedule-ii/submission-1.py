class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        outgoing = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            indegrees[a] += 1
            outgoing[b].append(a)

        q = deque()

        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)

        res = []

        while q:
            i = q.popleft()
            res.append(i)
            for j in outgoing[i]:
                indegrees[j] -= 1
                if indegrees[j] == 0:
                    q.append(j)

        return res if len(res) == numCourses else []