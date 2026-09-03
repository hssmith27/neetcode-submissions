class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            additions = []
            for array in res:
                new_array = array[:]
                new_array.append(num)
                additions.append(new_array)
            res += additions

        return res
