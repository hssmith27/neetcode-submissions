class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        max_occurences = 0
        for num in nums:
            freqs[num] += 1
            if freqs[num] > max_occurences:
                max_occurences = freqs[num]
        buckets = [[] for _ in range(max_occurences + 1)]

        for key, value in freqs.items():
            buckets[value] += [key]
        
        res = []

        last = len(buckets) - 1
        while k > 0:
            res += buckets[last]
            k -= len(buckets[last])
            last -= 1

        return res