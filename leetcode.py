class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = dict()
        myDict_t = dict()
        for char in s:
            if char in myDict:
                myDict[char] += 1
            else:
                myDict[char] = 1
        
        for char in t:
            if char in myDict_t:
                myDict_t[char] += 1
            else:
                myDict_t[char] = 1

        if myDict == myDict_t:
            return True
        return False
        

        