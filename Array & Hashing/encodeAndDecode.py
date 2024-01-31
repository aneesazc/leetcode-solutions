class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res    

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            print(length)
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length

        return res

Input: ["neet","code","love","you"]
Encode: "4#neet4#code4#love3#you"
Decode: ["neet","code","love","you"]
