# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None

        if not list1:
            return list2

        if not list2:
            return list1

        dummy_node:ListNode = ListNode()
        temp_node:ListNode = dummy_node
        current_node_1:ListNode = list1
        current_node_2:ListNode = list2

        while current_node_1 and current_node_2:

            is_value_less_than:bool = current_node_1.val < current_node_2.val

            if is_value_less_than:
                temp_node.next = current_node_1
                current_node_1 = current_node_1.next
            else:
                temp_node.next = current_node_2
                current_node_2 = current_node_2.next

            temp_node = temp_node.next

        if current_node_1:

            while current_node_1:
                temp_node.next = current_node_1
                current_node_1 = current_node_1.next
                temp_node = temp_node.next
        
        if current_node_2:

            while current_node_2:
                temp_node.next = current_node_2
                current_node_2 = current_node_2.next
                temp_node = temp_node.next
                
        return dummy_node.next
        