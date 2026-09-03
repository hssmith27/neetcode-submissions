class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Maps second number needed to index
        diffs = {}

        for i in range(len(nums)):
            if nums[i] in diffs:
                return [diffs[nums[i]], i]
            diffs[target - nums[i]] = i
            
        return [-1, -1]