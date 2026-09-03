class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def helper(i, total, cur, res):
            if total == target:
                res.add(tuple(cur))
            elif total < target and i < len(candidates):
                helper(i + 1, total + candidates[i], cur + [candidates[i]], res)
                helper(i + 1, total, cur, res)

        helper(0, 0, [], res)
        return [list(array) for array in res]