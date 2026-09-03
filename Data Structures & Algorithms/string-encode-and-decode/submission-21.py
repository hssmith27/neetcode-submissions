class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        sub_s = s
        while len(sub_s) > 0:
            i = 0
            while sub_s[i].isdigit():
                i += 1
            if (i != 0):
                count = int(sub_s[:i])
                print(sub_s[i + 1:i + 1+ count])
                res.append(sub_s[i + 1:i + 1 + count])
                sub_s = sub_s[i + 1 + count:]
            else:
                res.append('')
                sub_s = sub_s[1:]
        return res
