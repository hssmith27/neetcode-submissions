class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            prepend_word = str(length) + "#" + word
            res += prepend_word
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            start = i
            while s[i] != "#":
                i += 1

            length = int(s[start: i])
            i += 1

            word = s[i: i + length]
            res.append(word)
            i += length
            
        return res
