class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        outgoing = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            outgoing[b].append(a)
            indegrees[a] += 1

        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        while q:
            for i in range(len(q)):
                j = q.popleft()
                for k in outgoing[j]:
                    indegrees[k] -= 1
                    if indegrees[k] == 0:
                        q.append(k)

        return sum(indegrees) == 0