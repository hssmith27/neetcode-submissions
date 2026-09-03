class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)

        def valid_decoding(i, j):
            if i < 0 or j > len(s) or i >= j:
                return False
            sub = s[i:j]
            if len(sub) == 1:
                return sub in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            return sub[0] in ["1", "2"] and int(sub) <= 26
        
        dp[0] = 1 if valid_decoding(0, 1) else 0
        if len(s) > 1:
            total = 0
            if dp[0] != 0:
                if valid_decoding(1, 2):
                    total += 1
                if valid_decoding(0, 2):
                    total += 1
            dp[1] = total

        i = 2
        while i < len(s):
            total = 0
            if valid_decoding(i, i + 1):
                total += dp[i - 1]
            if valid_decoding(i - 1, i + 1):
                total += dp[i - 2]
            dp[i] = total
            i += 1
        print(dp)
        return dp[len(s) - 1]
            