class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        myString = ""
        for i in s:
            if i.isalnum():
                myString += i
        if myString == myString[::-1]:
            return True
        return False
