class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calc_dist(point):
            return math.sqrt(point[0] ** 2 + point[1] ** 2)

        distances = []
        for point in points:
            heapq.heappush(distances, (calc_dist(point), point))

        res = []
        while k > 0:
            res.append(heapq.heappop(distances)[1])
            k -= 1

        return res