# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        node = head
        prev = None

        while(node):
            next = node.next
            if(node.val == val and node == head):
                head = next
            elif(node.val == val):
                prev.next = next
            elif(node == head):
                prev = head
            else:
                prev = prev.next
            node = next
        
        return head