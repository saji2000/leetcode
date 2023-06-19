# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        remain = head.next.next
        new_head = head.next
        new_head.next = head
        head.next = self.swapPairs(remain)

        return new_head