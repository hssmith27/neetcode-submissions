class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = {}
        longest = 0
        for num in nums:
            values[num] = values.get(num, 0) + 1

        for key, value in values.items():
            current = key
            length = 1
            while values.get(current + 1, 0) != 0:
                length += 1
                current += 1
            if length > longest:
                longest = length

        return longest