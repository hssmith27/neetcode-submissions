class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r] 
                if total == 0:
                    triplets.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        
        return [list(triplet) for triplet in triplets]