# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
        """
        if head and head.next:            
            this_node = head.next
            prev_aux = head
            last_odd = head
            i = 2
            while this_node:
                if i % 2 == 1:
                    prev_aux.next = this_node.next
                    this_node.next = last_odd.next
                    last_odd.next = this_node
                    last_odd = this_node
                    this_node = prev_aux.next
                else:
                    prev_aux = this_node
                    this_node = this_node.next
                i+=1
        return head 

