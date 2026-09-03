class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        nums = sorted(nums)

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return [list(item) for item in res]

