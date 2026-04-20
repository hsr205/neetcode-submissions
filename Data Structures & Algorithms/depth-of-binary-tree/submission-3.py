# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        def dfs(node:Optional[TreeNode]) -> int:

            if not node:
                return 0

            
            left_tree_result:int = dfs(node.left) + 1
            right_tree_result:int = dfs(node.right) + 1

            return max(left_tree_result, right_tree_result)


        return dfs(node=root)
        