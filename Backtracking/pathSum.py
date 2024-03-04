# not the most prefered way
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         currSum = [0]
#         def leafPath(root, currSum):
#             if not root:
#                 return False
#             currSum[0] += root.val

#             if (not root.left and not root.right) and (currSum[0] == targetSum):
#                 return True
#             if leafPath(root.left, currSum):
#                 return True
#             if leafPath(root.right, currSum):
#                 return True
#             currSum[0] -= root.val
#             return False

#         return leafPath(root, currSum)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def leafPath(root, currSum):
            if not root:
                return False

            currSum += root.val  # Update the running sum by adding the current node's value

            # Check if the current node is a leaf and its value completes the path sum
            if not root.left and not root.right and currSum == targetSum:
                return True

            # Recursively check the left and right subtrees
            return leafPath(root.left, currSum) or leafPath(root.right, currSum)

        return leafPath(root, 0)  # Start with a sum of 0
'''
In the modified version of the code, currSum is passed directly into each recursive call as an argument, 
and each call gets its own separate copy of currSum because integers are immutable in Python. 
When you pass currSum + root.val to the recursive call, it does not change the original currSum in the current function's scope. 
Each path (left and right) gets a fresh version of currSum based on the current path's history, 
not affecting each other or the parent calls. Therefore, you don't need to subtract root.val after each recursive call, because each call's currSum is independent.
'''






        
