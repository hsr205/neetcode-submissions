from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result_list:list[list] = []

        queue: deque = deque([root])

        while queue:

            temp_list:list[int] = []

            for element in queue:
                temp_list.append(element.val)            

            for index in range(0, len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result_list.append(temp_list)

        return result_list