class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        lower = s.lower()

        while left < right:
            while left < len(s) and not lower[left].isalnum():
                left += 1
            while right >= 0 and not lower[right].isalnum():
                right -= 1
            if (left < len(s) and right > 0) and lower[left] != lower[right]:
                return False
            left += 1
            right -= 1

        return True