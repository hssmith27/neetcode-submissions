class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative = [-stone for stone in stones]
        heapq.heapify(negative)
        while len(negative) > 1:
            x = heapq.heappop(negative)
            y = heapq.heappop(negative)
            if y > x:
                heapq.heappush(negative, x - y)

        return -negative[0] if len(negative) == 1 else 0
