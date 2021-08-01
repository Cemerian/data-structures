# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Removes the nth node from the end, for example if n == 1, removes the last node of the list.
    Returns the remaining list.
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first_pointer = head
        for i in range(n):
            first_pointer = first_pointer.next
        if first_pointer is None:
            head = head.next
        else:
            second_pointer = head
            while first_pointer.next:
                first_pointer = first_pointer.next
                second_pointer = second_pointer.next
            second_pointer.next = second_pointer.next.next
        return head