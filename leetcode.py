# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)

        while queue:
            same_level = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                same_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            ans.append(same_level)

        return ans

                