class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for i in strs:
            sorted_word = "".join(sorted(i))
            groups[sorted_word].append(i)

        return list(groups.values())
