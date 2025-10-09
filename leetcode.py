from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for s in strs:
            sorted_word = "".join(sorted(s))
            hash_map[sorted_word].append(s)

        return list(hash_map.values())