class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s):
            if not s:
                return False
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1 
            return True

        def dfs(cur, curString, idx):
            if idx >= len(s):
                if not curString:
                    res.append(cur.copy())
                return
            curString += s[idx]
            if isPalindrome(curString):
                cur.append(curString)
                dfs(cur, "", idx + 1)
                cur.pop()
            dfs(cur, curString, idx + 1)

        dfs([], "", 0)
        return res