# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p and q or p and not q:
            return False

        list_1:list[TreeNode] = []
        list_2:list[TreeNode] = []

        def dfs(node:TreeNode, list_obj:list):
            
            list_obj.append(node)

            if not node:
                return

            dfs(node.left, list_obj)
            dfs(node.right, list_obj)

        dfs(p, list_1)
        dfs(q, list_2)

        if len(list_1) != len(list_2):
            return False

        is_same:bool = False

        for index in range(0, len(list_1)):

            value_1 = list_1[index]
            value_2 = list_2[index]

            if not value_1 and value_2 or value_1 and not value_2:
                return False

            if not value_1 and not value_2:
                continue

            if value_1.val == value_2.val:
                is_same = True
            else:
                return False

        return is_same
        