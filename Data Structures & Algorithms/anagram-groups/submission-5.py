class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = {}
        res = []
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in strings:
                strings[sorted_string] = [string]
            else:
                strings[sorted_string] = strings[sorted_string] + [string]
        
        for key, value in strings.items():
            res.append(value)


        return res
            