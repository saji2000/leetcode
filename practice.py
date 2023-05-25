class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if(index < 0 or index >= self.size):
            return -1
        curr = self.head

        for i in range(index):
            curr = curr.next

        return curr.value

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:

        node =  Node(val)

        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.addAtHead(val)

        else:
            node = Node(val)
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            
            node.next = curr.next
            curr.next = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)