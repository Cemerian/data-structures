# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Given a linked list, returns the node in which a cycle starts.
    Returns None if there are no cycles.
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        cycle_found = False
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                cycle_found = True
                break
        if cycle_found:
            new_pointer = head
            while new_pointer != fast_pointer:
                new_pointer = new_pointer.next
                fast_pointer = fast_pointer.next
            return fast_pointer
        return None
