class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                elif total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
        return list(res)
