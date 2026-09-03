class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        diffs = 0
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
                diffs += 1
        
        for letter in t:
            if letter in letters:
                letters[letter] -= 1
                if letters[letter] == 0:
                    diffs -= 1
                elif letters[letter] < 0:
                    return False
            else:
                return False

        return diffs == 0
        
