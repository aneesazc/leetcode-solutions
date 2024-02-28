#Time and Space- O(n) and O(logn) best case
# Remember, the space complexity is mainly determined by the height of the tree 
# since it dictates the maximum number of calls on the call stack (i.e., the maximum depth of the recursion).



# Recursice- inorder dfs
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # This list will hold the number of nodes visited and the kth smallest value.
        result = [0, None]

        def helper(node):
            # Base case: If node is None, return immediately (end of branch).
            if not node:
                return
            
            # Traverse the left subtree.
            helper(node.left)
            
            # Increment the count since we've visited another node.
            result[0] += 1
            
            # Check if the current node is the kth smallest.
            if result[0] == k:
                result[1] = node.val
                # Return from the function to stop further traversal.
                return
            
            # Only proceed to traverse the right subtree if we haven't found the kth element.
            helper(node.right)

        # Start the recursive in-order traversal from the root.
        helper(root)
        # The second element in the result list holds the kth smallest value.
        return result[1]


'''
Now I get it. I kept forgetting how inorder traversal works, I thought we would start at root, 
and count value would start from there, then we would go left and increase and go left and increase and so on. 
So it didnt make sense how we would find the kth smallest element.
But with inorder we actually start the count at the left most element itself because of how the recursion works inorder and now it makes sense

In the case of in-order traversal, each node ensures that:

1. Its left subtree is fully explored before dealing with the node itself (ensuring all smaller elements are counted first).
2. It deals with its own value (where you increment your counter).
3. Its right subtree is explored after its own value (ensuring all larger elements are counted after).
'''
