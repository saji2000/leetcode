# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(not head or not head.next):
            return False
        
        i = head
        j = head.next

        while(i != j):
            if(not j or not j.next):
                return False
            j = j.next.next
            i = i.next

        return True
