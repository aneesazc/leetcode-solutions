# O(n * m)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping countChar to list of Anagrams

        for s in strs:
            count = [0] * 26 # a....z

            for c in s:
                count[ord(c) - ord("a")] += 1  # this lets us map a -> 0 and z -> 25
                # c -> 99 - 97 = 2
                # b -> 98 - 97 = 1
                # a -> 97 - 97 = 0 and so on

            res[tuple(count)].append(s)  # python doesn't allow list as keys, so turn it into tuple

        return res.values()

# The defaultdict is designed to automatically create a new entry 
# with a default value when a non-existent key is accessed, 
# which is why you don't need to check for the key's existence in that case.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            count = [0] * 26 # a .... z
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        
        return list(res.values())

# can use either list(res.values()) or res.values
