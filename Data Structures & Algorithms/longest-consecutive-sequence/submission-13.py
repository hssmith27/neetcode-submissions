class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs = defaultdict(int)
        res = 0

        for num in nums:
            if seqs[num] == 0:
                seqs[num] = 1 + seqs[num - 1] + seqs[num + 1]
                seqs[num - seqs[num - 1]] = seqs[num]
                seqs[num + seqs[num + 1]] = seqs[num]
                
                if seqs[num] > res:
                    res = seqs[num]
        return res