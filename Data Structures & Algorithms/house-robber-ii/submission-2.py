class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def opt(houses):
            rob1, rob2 = 0, 0
            for house in houses:
                temp = max(rob1 + house, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(opt(nums[:-1]), opt(nums[1:]))