# O(p + q) time
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, they are the same.
        if not p and not q:
            return True
        # If one is None and the other is not, they aren't the same.
        if not p or not q:
            return False
        # If the values of the nodes are different, they aren't the same.
        if p.val != q.val:
            return False
        
        # Recursively check the left and right children.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True # empty trees are technically equal

        if not p or not q or p.val != q.val:
            return False # if either trees are null or have different values means NOT equal

        # recursively check if the left subtrees and right subtrees are equal
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
