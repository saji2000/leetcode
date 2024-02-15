# Definition for singly-linked list.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return 
        
        curr = head

        while curr.next and curr.next.next:
            curr = curr.next.next
            head = head.next
            if curr == head:
                return True
        return False
        

        

