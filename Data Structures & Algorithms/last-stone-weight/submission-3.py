class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * -1 for stone in stones]
        
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if abs(first) > abs(second):
                heapq.heappush(stones, first - second)
            
        if not stones:
            return 0
        return stones[0] * (-1)
        
        