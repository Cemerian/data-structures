
class Node:
    def __init__(self,val: int ,next = None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size or index < 0:
            return -1
        aux_node = self.head
        i = 0
        while i < index:
            aux_node = aux_node.next
            i+=1
        return aux_node.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val, self.head)
        self.head = new_node
        self.size +=1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val,None)
        if self.size == 0:
            self.head = new_node
            return        
        aux_node = self.head
        i = 0
        while aux_node.next:
            aux_node = aux_node.next
            i+=1
        aux_node.next = new_node
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        elif index <= self.size and index > 0:
        
             new_node = Node(val)
             aux_node = self.head.next
             prev_aux = self.head
             i = 0
             while i < index - 1:
                prev_aux = aux_node
                aux_node = aux_node.next
                i+=1
             prev_aux.next = new_node
             new_node.next = aux_node
             self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= 0 and index < self.size:
            if index == 0:
                self.head = self.head.next
            else:
                i = 0
                prev_aux = None
                aux_node = self.head
                while i < index:
                    prev_aux = aux_node
                    aux_node = aux_node.next
                    i += 1
                prev_aux.next = aux_node.next
                aux_node.next = None
                self.size -= 1
    def print(self):
        """
        Prints the elements of the list.
        """
        if self.size == 0:
            print('empty list')
        else:
            aux_node = self.head
            elements = ''  
            while aux_node:
                element += str(aux_node.val) + '-->'
                aux_node = aux_node.next
            print(lis)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)