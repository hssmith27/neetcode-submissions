class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums, idx):
        if idx > len(nums):
            return
        if idx == len(nums):
            self.res.append(nums.copy())
            return
        for i in range(idx, len(nums)):
            selected = nums.pop(i)
            nums.insert(idx, selected)
            self.backtrack(nums, idx + 1)
            selected = nums.pop(idx)
            nums.insert(i, selected)
            
