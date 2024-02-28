#Time and Space- O(n) and O(n) worst case and O(h) avg case
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, minVal, maxVal):
            # Base case: If the node is None, then this is a valid subtree.
            if not node:
                return True
            
            # Check if the current node's value violates the BST rules.
            # The value must be strictly greater than minVal and less than maxVal.
            if node.val <= minVal or node.val >= maxVal:
                return False
            
            # Recursively validate the left and right subtrees.
            # For the left subtree, update maxVal to node.val because all values must be less than the current node.
            # For the right subtree, update minVal to node.val because all values must be greater than the current node.
            # Both subtrees must be valid for the current tree to be valid.
            return validate(node.left, minVal, node.val) and validate(node.right, node.val, maxVal)

        # Initialize minVal and maxVal with infinity bounds because initially, there are no limits.
        minVal = float("-inf")
        maxVal = float("inf")
        
        # Start the recursion with the root node.
        return validate(root, minVal, maxVal)
