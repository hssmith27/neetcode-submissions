class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = {}
        for num in nums:
            try:
                if values[num] == 1:
                    return True
            except:
                values[num] = 1
        return False
