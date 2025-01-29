class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        ordered = sorted(hashmap.items(), key = lambda x: x[1], reverse=True)

        top_k = []

        for i in ordered[:k]:
            top_k.append(i[0])
        
        return top_k
        