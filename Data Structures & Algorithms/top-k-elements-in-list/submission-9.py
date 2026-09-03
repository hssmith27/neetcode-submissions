class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counting occurences of each element
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        vals = [(-count, val) for val, count in counts.items()]
        heapq.heapify(vals)

        res = []
        for i in range(k):
            res.append(heapq.heappop(vals)[1])
        return res

