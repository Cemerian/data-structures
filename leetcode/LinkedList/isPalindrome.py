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
            while head_node.next:
                head_node.next = aux_node.next
                aux_node.next = head
                head = aux_node
                aux_node = head_node.next
        return head
    def isPalindrome(self, head: ListNode) -> bool:
        """
        Given the head of a singly linked list, return true if it is a palindrome.
        """
        if head is None or head.next is None:
            return true
        palindrome = True
        half_list = None
        fast_pointer = head
        slow_pointer = head
        while True:
            fast_pointer = fast_pointer.next.next
            if fast_pointer is None:
                 half_list = slow_pointer = slow_pointer.next
                break
            if fast_pointer.next is None:
                half_list = slow_pointer = slow_pointer.next.next
                break
            slow_pointer = slow_pointer.next
        self.reverseList(half_list)
        slow_pointer.next = None
        while half_list and palindrome:
            if half_list.val != head.val:
                palindrome = False
            head = head.next
            half_list = half_list.next
        return palindrome