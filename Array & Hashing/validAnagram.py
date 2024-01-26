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



class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
