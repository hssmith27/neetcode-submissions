class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_low = s.lower()
        s_final = re.sub(r'[^a-zA-Z0-9]', '', s_low)
        
        i = 0
        j = len(s_final) - 1
        while i <= j:
            if s_final[i] != s_final[j]:
                return False
            i += 1
            j -= 1
        return True