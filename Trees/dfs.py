class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root):
    if not root:
        return    
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return    
    postorder(root.left)
    postorder(root.right)
    print(root.val)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # Initialize the result list

        def helper(node):
            # Base case: if the node is None, just return
            if not node:
                return
            
            # Recursive traversal: left subtree -> node value -> right subtree
            helper(node.left)
            res.append(node.val)  # Add the node's value to the result list
            helper(node.right)

        helper(root)  # Start the helper function with the root node
        return res  # Return the populated list after traversal
