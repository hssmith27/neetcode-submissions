class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroes = 0
        res = []

        for num in nums:
            if num == 0:
                zeroes += 1
                if zeroes >= 2:
                    prod *= num
            else:
                prod *= num

        for num in nums:
            if zeroes >= 2:
                res.append(0)
            elif zeroes == 1:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(int(prod / num))
        return res