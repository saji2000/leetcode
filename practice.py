# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if(not head or not head.next):
            return None
        
        i = head
        j = head.next

        while (i.next):
            if(j == i):
                return j
            if(j.next):
                j = j.next
            else:
                i = i.next
                j = i.next
        return None
