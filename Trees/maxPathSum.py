# Time and Space- O(n) and O(h)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the result with root's value to handle edge cases like negative values
        res = [root.val]

        def dfs(node):
            if not node:
                return 0  # Base case: Null nodes contribute 0 to the path sum

            # Recursively find the maximum path sum in the left subtree.
            # If negative, discard it by taking max with 0, as we can opt not to include negative paths.
            leftMax = max(dfs(node.left), 0)

            # Recursively find the maximum path sum in the right subtree.
            rightMax = max(dfs(node.right), 0)

            # Update the global maximum result. It represents the maximum possible path sum WITH SPLIT where
            # the current node acts as the root of the path. This path can include left and/or right children (hence with split)
            res[0] = max(res[0], node.val + leftMax + rightMax)

            # Return the maximum sum of paths WITHOUT SPLIT ending at the current node; this value will be used
            # by the node's parent in its computation. Note we can only add one of leftMax or rightMax (hence without split)
            # to avoid creating paths that aren't connected.
            return node.val + max(leftMax, rightMax)

        dfs(root)  
        return res[0]



class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
