class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        myString = ""
        for i in s:
            if i.isalnum():
                myString += i
        return myString == myString[::-1]