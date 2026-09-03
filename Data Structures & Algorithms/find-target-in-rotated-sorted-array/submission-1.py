class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
                
        pivot = left

        def binary_search(left, right):
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            return -1
        
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        return binary_search(pivot, len(nums) - 1)

        return -1

        