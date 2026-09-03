class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            j = i
            k = i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if (k - j + 1) > resLen:
                    resIdx = j
                    resLen = k - j + 1
                j -= 1
                k += 1
            
            j = i
            k = i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if (k - j + 1) > resLen:
                    resIdx = j
                    resLen = k - j + 1
                j -= 1
                k += 1
        
        return s[resIdx:resIdx + resLen]