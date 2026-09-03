class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l, r = 0, 0
        maxChar = ""
        chars = defaultdict(int)

        while r < len(s):
            print(chars)
            nextChar = s[r]
            chars[nextChar] += 1

            # Update max char
            if maxChar == "" or chars[maxChar] < chars[nextChar]:
                maxChar = nextChar

            replacements = (r - l + 1) - chars[maxChar]
            
            # Shrink window if too many replacments
            while replacements > k and l < len(s):
                prevChar = s[l]
                chars[prevChar] -= 1
                l += 1
                if prevChar != maxChar:
                    replacements -= 1
                else:
                    maxChar = max(chars, key=chars.get)
                    replacements = (r - l + 1) - chars[maxChar]
                
            res = max(res, r - l + 1)
            r += 1

        return res