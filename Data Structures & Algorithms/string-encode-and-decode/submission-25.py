class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0

        while index < len(s):
            num = ""
            while s[index] != "#":
                num += s[index]
                index += 1
            num = int(num)
            index += 1

            res.append(s[index:index + num])
            index += num
        return res
