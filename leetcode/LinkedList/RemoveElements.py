# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        aux_node = head
        prev_aux = None
        while aux_node:
            if aux_node.val == val:
                if aux_node == head:
                    head = aux_node.next
                else:
                    prev_aux.next = aux_node.next
            else:
                prev_aux = aux_node
            aux_node = aux_node.next
        return head