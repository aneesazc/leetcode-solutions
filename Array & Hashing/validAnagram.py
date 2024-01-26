class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}

        for c in s:
            if c not in hashMap1:
                hashMap1[c] = 1
            else:
                hashMap1[c] += 1

        for c in t:
            if c not in hashMap2:
                hashMap2[c] = 1
            else:
                hashMap2[c] += 1

        return hashMap1 == hashMap2
