class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in closeToOpen:
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         hashMap = {")": "(", "}": "{", "]": "["}

#         for c in s:
#             if c not in hashMap:
#                 stack.append(c)
#             else:
#                 if stack and hashMap[c] == stack[-1]:
#                     stack.pop()
#                 else:
#                     return False
#         if not stack:
#             return True
#         else:
#             return False
