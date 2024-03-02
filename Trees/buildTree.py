class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: if either list is empty, we return None as there is no tree to construct
        if not preorder or not inorder:
            return None

        # The first element in preorder list is always the root of the tree
        root = TreeNode(preorder[0])

        # Find the position of the root in the inorder list; this index splits the tree into left and right subtrees
        mid = inorder.index(preorder[0])

        # Recursively build the left subtree using the left portion of inorder list (before 'mid') 
        # and the corresponding portion of preorder list (1 to 'mid' + 1 because preorder[0] is the root)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        # Recursively build the right subtree using the right portion of inorder list (after 'mid') 
        # and the corresponding portion of preorder list (from 'mid' + 1 to the end)
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # Return the root node of the constructed tree
        return root

'''
This method works because in inorder traversal, the left subtree's nodes come before the root, 
and in preorder traversal, the root comes first, followed by all nodes of the left subtree (in their own preorder), 
and then all nodes of the right subtree (in their own preorder).

The split for the left and right subtrees in preorder directly relates to the split in inorder based on the root found in preorder.

The inorder array tells us how many nodes are in each subtree (because the root splits inorder into left and right subtrees).

The preorder array gives us the order in which to build these subtrees (root first, then all left subtree, then all right subtree).

By applying these splits recursively, you construct the tree:
Build left subtree with preorder[1:mid + 1] and inorder[:mid] (where mid is the count of nodes in the left subtree or the index of the root in inorder).
Build right subtree with preorder[mid + 1:] and inorder[mid + 1:].
'''
