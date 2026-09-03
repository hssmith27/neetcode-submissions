class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = defaultdict(int)
        res = 0

        for num in nums:
            if lengths[num] != 0:
                continue
            lengths[num] = 1 + lengths[num + 1] + lengths[num - 1]
            lengths[num - lengths[num - 1]] = lengths[num]
            lengths[num + lengths[num + 1]] = lengths[num]
            res = max(res, lengths[num])

        return res