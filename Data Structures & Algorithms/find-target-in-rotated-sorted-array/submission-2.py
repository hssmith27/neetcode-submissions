class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Find the start of the sorted array
        while l < r:
            m = (r + l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        offset = l
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            offset_m = m + offset
            if offset_m >= len(nums):
                offset_m -= len(nums)
            print(l, r, m, offset_m)
            if nums[offset_m] == target:
                return offset_m
            elif nums[offset_m] > target:
                r = m - 1
            else:
                l = m + 1
            print(l, r, m, offset_m)
            print()
            

        return -1