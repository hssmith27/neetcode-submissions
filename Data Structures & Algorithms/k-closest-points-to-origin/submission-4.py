class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        def calc_distance(point):
            x1 = point[0]
            y1 = point[1]
            x2 = 0
            y2 = 0
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

        heap = []
        
        for point in points:
            dist = calc_distance(point)
            heapq.heappush(heap, [dist, point])
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res