class Solution:
    def isPalindrome(self, s: str) -> bool:
        myString = ""

        for i in s:
            if i.isalnum():
                myString += i
        myString = myString.lower()
        return myString == myString[::-1]