class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += (str(len(i))) + "#" + i
        print(encoded)
        return encoded

    def decode(self, s: str) -> list[str]:
        decoded = []
        i = 0
        while i < len(s):
            pos = s.find('#', i)
            length = int(s[i:pos])
            decoded.append(s[pos + 1: pos + 1 + length])
            i = pos + length + 1
        return decoded




solution = Solution()

encoded = solution.encode(["neet","code","love","you"])
solution.decode(encoded)