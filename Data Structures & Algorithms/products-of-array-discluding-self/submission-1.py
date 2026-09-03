class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                product *= num
        if zeros > 1:
            return [0] * len(nums)
        for num in nums:
            if zeros == 1:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(product // num)
        return res