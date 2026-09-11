class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesC = []
        for stone in stones:
            stonesC.append(-stone)

        heapq.heapify(stonesC)

        while len(stonesC) > 1:
            x = -heapq.heappop(stonesC)
            y = -heapq.heappop(stonesC)
            if x > y:
                heapq.heappush(stonesC, -(x - y))
            elif y > x:
                heapq.heappush(stonesC, -(y - x))


        return 0 if not stonesC else -stonesC[0]