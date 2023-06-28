# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        val = val
        next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         val = val
#         next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ans = None

        if(not list2):
            return list1
        elif(not list1):
            return list2
        
        
        if(list1.val <= list2.val):
            ans = list1
            ans.next = self.mergeTwoLists(list1.next, list2)

        else:
            ans = list2
            ans.next = self.mergeTwoLists(list1, list2.next)

        return ans




