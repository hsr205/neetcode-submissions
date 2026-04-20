# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        result_value = True

        def dfs(node) -> int:
            nonlocal result_value
            if not node:
                return 0

            left_tree_height = dfs(node.left)
            right_tree_height = dfs(node.right)

            height_diff = abs(left_tree_height - right_tree_height)

            if height_diff > 1:
                result_value = False

            return 1 + max(left_tree_height, right_tree_height)

        dfs(root)
        
        return result_value
        