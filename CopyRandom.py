class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        copy = {}

        curr = head

        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            copy[curr].next = copy.get(curr.next)
            copy[curr].random = copy.get(curr.random)
            curr = curr.next

        return copy[head]
