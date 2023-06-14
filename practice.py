# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(-1)
        sum = head
        carry = 0

        while(l1 or l2 or carry):

            if(l1):
                carry += l1.val
                l1 = l1.next
            if(l2):
                carry += l2.val
                l2 = l2.next

            sum.next = ListNode(carry % 10)
            sum = sum.next
            if(carry >= 10):
                carry = 1
            else:
                carry = 0

        return head.next