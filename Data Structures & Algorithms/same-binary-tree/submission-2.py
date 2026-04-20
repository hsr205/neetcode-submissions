# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def dfs(root_1:Optional[TreeNode], root_2:Optional[TreeNode]) -> bool:

            if not root_1 and not root_2:
                return True

            if not root_1 and root_2 or root_1 and not root_2 or root_1.val != root_2.val:
                return False

            is_left_tree:bool=dfs(root_1.left, root_2.left)
            is_right_tree:bool=dfs(root_1.right, root_2.right)

            return is_left_tree and is_right_tree
            

        return dfs(root_1=p, root_2=q)

