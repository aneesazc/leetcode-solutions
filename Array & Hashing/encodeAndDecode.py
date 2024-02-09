# Time- O(
class Solution:
    def encode(self, strs: List[str]) -> str:
        # Encode a list of strings into a single string with each string prefixed by its length and a delimiter "#".
        res = ""
        for s in strs:
            # For each string, append its length, a "#" delimiter, and then the string itself.
            res += str(len(s)) + "#" + s
        return res
        # Example output: "4#neet4#code4#love3#you"

    def decode(self, s: str) -> List[str]:
        # Decode a single string back into a list of strings based on the encoding scheme.
        res = []
        i = 0  # Start index of the current segment

        while i < len(s):
            j = i  # Find the index of "#" to determine the length of the next string

            # Locate the next "#" delimiter to extract the length of the encoded string.
            while s[j] != "#":
                j += 1

            # Extract the length of the string (before the "#").
            length = int(s[i:j])  # Correction: parse the length using s[i:j] instead of s[i]

            # Extract the string using the length found and add it to the result list.
            res.append(s[j+1: j+1+length])

            # Move to the start of the next encoded string segment.
            i = j + 1 + length
        return res



Input: ["neet","code","love","you"]
Encode: "4#neet4#code4#love3#you"
Decode: ["neet","code","love","you"]
