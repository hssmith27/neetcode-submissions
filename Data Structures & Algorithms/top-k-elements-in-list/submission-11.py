class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the number of each element
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        maxCount = max(counts.values())

        buckets = [[] for _ in range(maxCount)]

        for val, count in counts.items():
            buckets[count - 1].append(val)

        res = []

        for i in range(len(buckets) - 1, -1, -1):
            if len(res) < k:
                res += buckets[i]
        return res



        
