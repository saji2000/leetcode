class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(index, cur, total):
            if total == target:
                result.append(cur.copy())
                return
            if index >= len(candidates) or total > target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                cur.append(candidates[i])
                backtrack(i + 1, cur, total + candidates[i])
                cur.pop()
        
        backtrack(0, [], 0)
        return result
        