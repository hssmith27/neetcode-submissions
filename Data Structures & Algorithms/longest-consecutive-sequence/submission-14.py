class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs = defaultdict(int)
        max_len = 0
        
        for num in nums:
            if seqs[num] == 0:
                seqs[num] = 1 + seqs[num - 1] + seqs[num + 1]
                seqs[num - seqs[num - 1]] = seqs[num]
                seqs[num + seqs[num + 1]] = seqs[num]
                max_len = max(seqs[num], max_len)

        return max_len