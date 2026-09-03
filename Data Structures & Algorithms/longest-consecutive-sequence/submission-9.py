class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs = {}
        if len(nums) == 0:
            return 0

        for num in nums:
            if num not in seqs:
                seqs[num] = 1
                if num - 1 in seqs:
                    seqs[num] = seqs[num] + seqs[num - 1] 
                if num + 1 in seqs:
                    seqs[num] = seqs[num] + seqs[num + 1]
                if num - 1 in seqs:
                    seqs[num - seqs[num - 1]] = seqs[num]
                if num + 1 in seqs:
                    seqs[num + seqs[num + 1]] = seqs[num]

        return max(seqs.values())

        