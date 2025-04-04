"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
            
        hashMap = {}
        node = head
        
        while node:
            hashMap[node] = ListNode(node.val)
            node = node.next
        
        node = head
        while node:
            hashMap[node].next = hashMap.get(node.next)
            hashMap[node].random = hashMap.get(node.random)
            node = node.next
        
        return hashMap[head]
        

