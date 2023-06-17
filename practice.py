# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        my_list = {}
        
        curr = head

        while curr:

            node = Node(curr.val)

            my_list[curr] = node

            curr = curr.next
        
        curr = head

        while curr:

            node = my_list[curr]

            if(curr.next):
                node.next = my_list[curr.next]
            
            if(curr.random):
                node.random = my_list[curr.random]

            curr = curr.next
        
        return my_list[0]