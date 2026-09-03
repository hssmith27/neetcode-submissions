class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(cur, idx):
            if idx == len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[idx])
            dfs(cur, idx + 1)
            cur.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(cur, idx + 1)

        dfs([], 0)
        return res