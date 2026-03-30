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
            
            cur.append(candidates[index])
            backtrack(index  + 1, cur, total + candidates[index])
            cur.pop()

            while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, cur, total)
        
        backtrack(0, [], 0)
        return result