class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        right = 0

        majority_count = 0
        chars = {}

        while right < len(s):
            next_char = s[right]
            chars[next_char] = chars.get(next_char, 0) + 1

            if chars[next_char] > majority_count:
                majority_count = chars[next_char]
            
            while (right - left + 1) - majority_count > k:
                chars[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1

        return res