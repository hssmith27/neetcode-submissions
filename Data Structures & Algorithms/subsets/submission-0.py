import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            current = copy.deepcopy(res)
            for i in range(len(current)):
                current[i].append(num)
                res.append(current[i])
        return res