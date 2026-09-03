class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[l] < nums[r]:
                break
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                print("W")
                r = m
                l += 1
            
        pivot = l
        
        def binary_search(start, end):
            while start <= end:
                m = (start + end) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    start = m + 1
                else:
                    end = m - 1
                
            return -1

        first = binary_search(0, pivot - 1)
        if first != -1:
            return first

        return binary_search(pivot, len(nums) - 1)