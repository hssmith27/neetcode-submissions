class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(cur, l, r):
            if l == len(s):
                res.append(cur)
                return
            if l > len(s) or r > len(s):
                return
            
            if self.isPalindrome(s, l, r - 1):
                dfs(cur + [s[l:r]], r, r + 1)
            dfs(cur, l, r + 1)

        dfs([], 0, 1)
        return res

    def isPalindrome(self, string, l, r):
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True
            