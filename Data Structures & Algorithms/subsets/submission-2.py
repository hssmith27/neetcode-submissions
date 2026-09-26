class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i, cur):
            if i >= len(nums):
                res.append(cur)
                return
            backtrack(i + 1, cur[:])
            backtrack(i + 1, cur[:] + [nums[i]])

        backtrack(0, [])
        return res