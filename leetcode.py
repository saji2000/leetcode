class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, cur, total):
            if sum(cur) == target:
                result.append(cur.copy())
                return
            if index == len(candidates) or sum(cur) > target:
                return

            cur.append(candidates[index])
            backtrack(index, cur, total + candidates[index])
            cur.pop()

            backtrack(index + 1, cur, total)

        backtrack(0, [], 0)
        return result
