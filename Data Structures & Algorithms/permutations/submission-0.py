class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def permuteH(nums, current, res):
            if not nums:
                res.append(current)
            else:
                for i in range(len(nums)):
                    new_current = current.copy()
                    new_current.append(nums[i])
                    permuteH(nums[0:i] + nums[i + 1:], new_current, res)


        permuteH(nums, [], res)

        return res
