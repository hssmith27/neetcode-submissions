class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            keys[sorted_word] = keys.get(sorted_word, []) + [word]

        res = []

        for sorted_word in keys:
            res.append(keys[sorted_word])

        return res