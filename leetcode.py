class Solution:
    def isValid(self, s: str) -> bool:
        tags = {'(': ')', '[': ']', '{': '}'}
        queue = []

        for i in s:
            if i in '({[':
                queue.append()
            elif len(queue) == 0 or i != tags[queue.pop()]:
                return False
        return len(queue) == 0