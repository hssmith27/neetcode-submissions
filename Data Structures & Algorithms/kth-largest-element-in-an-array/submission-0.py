class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-1 * num for num in nums]
        heapq.heapify(maxHeap)

        i = 1
        while i < k:
            heapq.heappop(maxHeap)
            i += 1

        return heapq.heappop(maxHeap) * -1