class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        for s in strs:
            s_sorted = sorted(s)
            is_placed = False
            for i in range(len(result)):
                if sorted(result[i][0]) == s_sorted:
                    result[i].append(s)
                    is_placed = True
            if not is_placed:
                result.append([s])

        return result