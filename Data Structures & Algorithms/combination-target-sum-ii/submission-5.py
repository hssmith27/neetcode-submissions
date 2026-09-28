class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def backtrack(i, cur, total):
            if i >= len(candidates) or total > target:
                return
            if total + candidates[i] == target:
                res.add(tuple(cur[:] + [candidates[i]]))
            else:
                backtrack(i + 1, cur[:] + [candidates[i]], total + candidates[i])
                while i < len(candidates) - 1 and candidates[i + 1] == candidates[i]:
                    i += 1
                backtrack(i + 1, cur[:], total)

        backtrack(0, [], 0)
        realRes = []
        for item in res:
            realRes.append(list(item))

        return realRes