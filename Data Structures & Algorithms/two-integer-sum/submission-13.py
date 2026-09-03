class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in diffs:
                return [diffs[nums[i]], i]
            diffs[diff] = i
        return [-1, -1]