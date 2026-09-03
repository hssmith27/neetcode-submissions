class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = len(t)
        res = ""

        if len(t) > len(s):
            return ""

        charS = {}
        charT = {}

        matches = 0
        neededMatches = 0

        for i in range(len(t)):
            charS[s[i]] = charS.get(s[i], 0) + 1
            if t[i] not in charT:
                neededMatches += 1
            charT[t[i]] = charT.get(t[i], 0) + 1
        
        for key, value in charT.items():
            if charS.get(key, -1) >= value:
                matches += 1

        while right <= len(s):
            print(s[left:right])
            while matches == neededMatches and left < len(s):
                substring = s[left:right]
                if len(substring) < len(res) or not res:
                    res = substring

                if s[left] in charT:
                    if charS[s[left]] == charT[s[left]]:
                        matches -= 1
                charS[s[left]] = charS[s[left]] - 1
                left += 1
            
            if len(s) != right:
                charS[s[right]] = charS.get(s[right], 0) + 1
                if s[right] in charT:
                    if charS[s[right]] == charT[s[right]]:
                        matches += 1
            right += 1

        return res


