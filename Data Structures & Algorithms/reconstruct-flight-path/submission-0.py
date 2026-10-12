class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for src, dest in sorted(tickets)[::-1]:
            adj[src].append(dest)

        stack = ["JFK"]
        res = []

        while stack:
            curr = stack[-1]
            if not adj[curr]:
                res.append(stack.pop())
            else:
                stack.append(adj[curr].pop())

        return res[::-1]