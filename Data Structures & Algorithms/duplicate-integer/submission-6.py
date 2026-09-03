class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = {}
        for num in nums:
            if num in values:
                return True
            values[num] = 1
        return False
