#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        cycle_found = False
        slow_pointer = head
        fast_pointer = head.next
        steps = 0
        while cycle_found == False and fast_pointer:
            """
            Checks if the list has a cycle
            """
            if fast_pointer == slow_pointer:
                cycle_found = True
            else:
                fast_pointer = fast_pointer.next
                if steps % 2 == 0:
                    slow_pointer = slow_pointer.next
            steps += 1
        return cycle_found
            


