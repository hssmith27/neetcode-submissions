class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freqs = defaultdict(list)
        maxFreq = 0

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for num in counts.keys():
            if counts[num] > maxFreq:
                maxFreq = counts[num]
            freqs[counts[num]].append(num)

        res = []
        i = 0
        while i < k:
            while maxFreq not in freqs:
                maxFreq -= 1

            res += freqs[maxFreq]
            i += len(freqs[maxFreq])
            maxFreq -= 1

        return res
            

        