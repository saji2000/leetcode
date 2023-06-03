# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if(not head or not head.next):
            return None
        
        visited = set()
        i = head 

        while(i):
            if(i not in visited):
                visited.add(i)
            elif(i in visited):
                return i
            i = i.next
        
        return None
