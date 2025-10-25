class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_string = ""
        for i in s:
            if i.isalnum():
                my_string += i
        
        my_string = my_string.lower()

        return my_string == my_string[::-1]