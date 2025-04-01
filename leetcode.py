# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return
        
        node = head
        length = 1

        while node.next:
            length += 1
            node = node.next
        
        pos = length - n
        if pos == 0:
            return head.next

        node = head
        i = 0

        while i != pos - 1:
            node = node.next
            i += 1
        
        node.next = node.next.next 

        return head
                
        
        