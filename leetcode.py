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
        hashmap = {}

        node = head
        newHead = Node(0)
        newNode = newHead

        while node:
            newNode.next = Node(node.val, None, None)
            hashmap[node] = newNode.next
            newNode = newNode.next
            node = node.next

        node = head
        newNode = newHead.next

        while node:
            if node.random:
                newNode.random = hashmap[node.random]
            node = node.next
            newNode = newNode.next
        
        return newHead.next
        