# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        length = 0
        node = head
        
        while node:
            node = node.next
            length += 1
        
        n = length - n
        
        if n == 0:
            return head.next
        
        node = head
        
        for i in range(0, n - 1):
            node = node.next
        
        node.next = node.next.next
        
        return head

