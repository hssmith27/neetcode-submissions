class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def combinationSumH(i, total, cur):
            if total == target:
                res.append(cur.copy())
            elif total < target and i < len(nums):
                cur.append(nums[i])
                combinationSumH(i, total + nums[i], cur)
                cur.pop()
                combinationSumH(i + 1, total, cur)
        
        combinationSumH(0, 0, [])
        return res