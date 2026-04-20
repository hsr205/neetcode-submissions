# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visited_nodes:list[ListNode] = []

        while head:
            
            if head in visited_nodes:
                return True
            
            visited_nodes.append(head)
            head = head.next

        return False
        