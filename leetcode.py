# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side = []

        if not root:
            return right_side

        queue = collections.deque()

        queue.append(root)

        while queue:
            same_level = []

            size = len(queue)
            for _ in range(size):
                node = queue.popleft()

                same_level.append(node.val)

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

            right_side.append(same_level[0])
        
        return right_side