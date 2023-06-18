# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        

        tail = head 
        length = 1

        while tail.next:
            tail = tail.next
            length += 1

        k = k % length

        if(k == 0):
            return head

        position = length - k - 1
        
        node = head

        for i in range(position):

            node = node.next

        new_head = node.next
        node.next = None
            
        tail.next = head
        return new_head