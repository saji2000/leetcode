# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ans = ListNode(0)
        ans_node = ans

        while(list1 and list2):
            if(list1.val <= list2.val):
                ans_node.next = list1
                list1 = list1.next
            else:
                ans_node.next = list2
                list2 = list2.next
            ans_node = ans_node.next
        
        if(list1):
            ans_node.next = list1
        else:
            ans_node.next = list2

        return ans.next
