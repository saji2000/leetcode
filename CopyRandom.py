class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        my_dict = {}

        curr = head

        while curr:
            my_dict[curr] = ListNode(curr.val)
            curr = curr.next

        curr = head

        while curr:
            my_dict[curr].next = my_dict.get(curr.next)
            my_dict[curr].random = my_dict.get(curr.random)
            curr = curr.next

        return my_dict[head]
