# Definition for singly-linked list.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return 
        mySet = set()

        while head.next:
            if head in mySet:
                return True
            mySet.add(head)
            head = head.next
        return False
        

        

