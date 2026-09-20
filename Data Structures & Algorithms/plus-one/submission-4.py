class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        remainder = 1
        while remainder:
            val = digits[i]
            total = val + remainder
            remainder = 0
            if total <= 9:
                digits[i] = total
            else:
                digits[i] = total % 10
                remainder = total // 10
            
            if i > 0:
                i -= 1
            elif remainder:
                digits.insert(0, 0)

        return digits