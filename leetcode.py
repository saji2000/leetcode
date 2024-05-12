class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + "#" + i
        return encoded
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            length_str = ""
            while s[i] != "#":
                length_str += s[i]
                i += 1
            number = int(length_str)
            decoded.append(s[i + 1 : i + 1 + number])            
            i += 1 + number
        return decoded