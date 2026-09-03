class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            vals[num] = vals.get(num, 0) + 1
        for num, cnt in vals.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            res += freq[i]
            if len(res) == k:
                return res

        