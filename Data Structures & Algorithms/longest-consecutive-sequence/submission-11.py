class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seq = {}

        for num in nums:
            if num in seq:
                continue
            seq[num] = 1
            if num + 1 in seq and num - 1 in seq:
                new_length = seq[num + 1] + seq[num - 1] + 1
                seq[num + seq[num + 1]] = new_length
                seq[num - seq[num - 1]] = new_length
            elif num + 1 in seq:
                new_length = 1 + seq[num + 1]
                seq[num] = new_length
                seq[num + seq[num + 1]] = new_length
            elif num - 1 in seq:
                new_length = 1 + seq[num - 1]
                seq[num] = new_length
                seq[num - seq[num - 1]] = new_length
        
        print(seq)
        return max(seq.values())