class Solution:
    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)

        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = self.gcd(n1, n2)

        return str1[:gcd_length]
