class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        freqs = [(-count, val) for val, count in counts.items()]

        heapq.heapify(freqs)

        res = []
        for i in range(k):
            res.append(heapq.heappop(freqs)[1])

        return res