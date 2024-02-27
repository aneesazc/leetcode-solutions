# Time and Space- O(logn) and O(1)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Initialize current node as root of the tree
        curr = root

        # Continue traversing the tree until the correct node is found
        while curr:
            # If both p and q are greater than current node's value,
            # it means both nodes are in the right subtree.
            if p.val > curr.val and q.val > curr.val:
                # Move to the right child of the current node.
                curr = curr.right
            # If both p and q are less than current node's value,
            # it means both nodes are in the left subtree.
            elif p.val < curr.val and q.val < curr.val:
                # Move to the left child of the current node.
                curr = curr.left
            # If neither of the above conditions are true, it means we have found
            # the split point: either one of p or q equals the current node, or
            # p and q lie on different sides of the current node. In either case,
            # the current node is the lowest common ancestor.
            else:
                # Return the current node as the lowest common ancestor.
                return curr
