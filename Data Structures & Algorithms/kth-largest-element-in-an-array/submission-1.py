class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        elements = []
        
        for num in nums:
            heapq.heappush(elements, num)
            while len(elements) > k:
                heapq.heappop(elements)

        return heapq.heappop(elements)