# Combined Complexity: Since you might perform an O(M) isSameTree check for each of the O(N) nodes in root, 
# the worst-case overall time complexity is O(N * M).

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base conditions: if subRoot is None, it's universally a subtree; if root is None, subRoot cannot be a subtree
        if not subRoot: return True
        if not root: return False

        # Check if trees rooted at the current node are identical
        if self.isSameTree(root, subRoot):
            return True
        
        # Recursively check if subRoot is a subtree of the left or right subtree of the current node
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        # If both trees are empty, they are identical
        if not p and not q:
            return True
        # If both trees are non-empty, compare their values and the values of their subtrees
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # If one tree is empty and the other is not, or if their values differ, the trees are not identical
        else:
            return False
