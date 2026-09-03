class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort(reverse=True)
        res = []
        self.combinationSumH(nums, target, [], res)
        return res
    
    def combinationSumH(self, nums, target, cur, res):
        if target == 0:
            res.append(cur)
        elif nums:
            self.combinationSumH(nums[1:], target, cur, res)
            if target - nums[0] >= 0:
                self.combinationSumH(nums, target - nums[0], cur + [nums[0]], res)
        