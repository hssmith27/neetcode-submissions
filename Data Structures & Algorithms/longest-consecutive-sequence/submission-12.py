class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seqs = defaultdict(int)
        
        for num in nums:
            if longest_seqs[num] == 0:
                longest_seqs[num] = 1
                if longest_seqs[num - 1] != 0 and longest_seqs[num + 1] != 0:
                    total_length = longest_seqs[num - 1] + longest_seqs[num + 1] + 1
                    longest_seqs[num - longest_seqs[num - 1]] = total_length
                    longest_seqs[num + longest_seqs[num + 1]] = total_length
                elif longest_seqs[num - 1] != 0:
                    longest_seqs[num] = longest_seqs[num - 1] + 1
                    longest_seqs[num - longest_seqs[num - 1]] = longest_seqs[num - 1] + 1
                elif longest_seqs[num + 1] != 0:
                    longest_seqs[num] = longest_seqs[num + 1] + 1
                    longest_seqs[num + longest_seqs[num + 1]] = longest_seqs[num + 1] + 1

        max_seq = 0
        for val in longest_seqs.values():
            if val > max_seq:
                max_seq = val
        
        return max_seq


