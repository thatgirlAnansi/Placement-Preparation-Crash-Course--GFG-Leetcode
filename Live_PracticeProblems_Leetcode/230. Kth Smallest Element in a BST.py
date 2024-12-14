class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Helper function for inorder traversal
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        # Perform inorder traversal and fetch the k-th smallest element
        return inorder(root)[k - 1]
