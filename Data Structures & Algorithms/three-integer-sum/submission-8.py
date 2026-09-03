class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == -nums[k]:
                    res.append([nums[i], nums[j], nums[k]])
                    prev = nums[i]
                    while i < len(nums) and nums[i] == prev:
                        i += 1
                elif nums[i] + nums[j] < -nums[k]:
                    i += 1
                else:
                    j -= 1

        return res
