class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            groups["".join(sorted(word))] = word

        return [groups.values()]
