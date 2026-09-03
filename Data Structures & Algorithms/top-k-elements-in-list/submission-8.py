class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        max_freq = 0

        for num in nums:
            freqs[num] += 1
            max_freq = max(max_freq, freqs[num])

        buckets = [[] for _ in range(max_freq + 1)]
        print(buckets)
        for key, value in freqs.items():
            buckets[value].append(key)
        
        last = len(buckets) - 1
        res = []

        while k > 0:
            if buckets[last] != []:
                res += buckets[last]
                k -= len(buckets[last])
            last -= 1
        
        return res
