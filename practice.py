# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans = ListNode(0)
        head = ans

        while list1 or list2:
            if not list1:
                head.next = list2
                return ans.next
            elif not list2:
                head.next = list1
                return ans.next
            if list1.val <= list2.val:
                head.next = ListNode(list1.val)
                list1 = list1.next
                head = head.next
            else:
                head.next = ListNode(list2.val)
                list2 = list2.next
                head = head.next

        return ans.next
