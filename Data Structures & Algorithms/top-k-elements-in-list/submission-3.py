class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        vals = {}
        for num in nums:
            if num in vals:
                vals[num] = vals[num] + 1
            else:
                vals[num] = 1
        maxes = []

        sorted_vals = sorted(vals.items(), key = lambda x: x[1], reverse = True)
        for i in range(k):
            res.append(sorted_vals[i][0])
        
        return res