# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        node = head
        nodes = []

        while(node):
            nodes.append(node.val)
            node = node.next
        
        for j in range(len(nodes)):
            if(nodes[j] != nodes[-j-1]):
                return False
            
        return True
