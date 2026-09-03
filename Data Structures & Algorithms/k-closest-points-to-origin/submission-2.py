class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        def calc_distance(point):
            return math.sqrt((point[0]) ** 2 + (point[1]) ** 2)

        for point in points:
            cur = [-calc_distance(point), point]
            if len(maxHeap) >= k:
                if cur[0] > maxHeap[0][0]:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, cur)
            else:
                heapq.heappush(maxHeap, cur)
        
        return [values[1] for values in maxHeap]