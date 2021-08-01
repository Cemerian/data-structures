# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            head_node = head
            aux_node = head_node.next
            while head_node.next != None:
                head_node.next = aux_node.next
                aux_node.next = head
                head = aux_node
                aux_node = head_node.next
        return head
            