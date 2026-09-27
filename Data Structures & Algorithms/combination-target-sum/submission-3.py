class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i, cur, total):
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            if i >= len(nums):
                return
            if total + nums[i] == target:
                res.append(cur[:] + [nums[i]])
            if total + nums[i] < target:
                backtrack(i, cur[:] + [nums[i]], total + nums[i])
            backtrack(i + 1, cur[:], total)

        backtrack(0, [], 0)
        return res