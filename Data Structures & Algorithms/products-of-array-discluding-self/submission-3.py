class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        product = 1

        res = []

        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                product *= num
        
        for num in nums:
            if zeroes > 1:
                res.append(0)
            elif zeroes == 1:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(int(product / num))

        return res