# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Given two linked lists, returns the node in which both lists intersect.
        Returns None if there is no intersection.
        """
        aux_nodeA = headA
        aux_nodeB = headB
        while aux_nodeA != aux_nodeB:
            if aux_nodeA is None:
                aux_nodeA = headB
            else aux_nodeA = aux_nodeA.next
            if aux_nodeB is None:
                aux_nodeB = headA
            else aux_nodeB = aux_nodeB.next
        return aux_nodeA

               
            