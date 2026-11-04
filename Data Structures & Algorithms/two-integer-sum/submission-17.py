class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: the value needed to get to target, value: index
        diffs = {}

        for i in range(len(nums)):
            if nums[i] in diffs:
                return [diffs[nums[i]], i]
            diff = target - nums[i]
            diffs[diff] = i

        return [-1, -1]

