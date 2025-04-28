# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res
        
        q = collections.deque()
        q.append(root)

        while q:
            level_size = len(q)
            same_level = []
            print(same_level)
            for i in range(level_size):
                node = q.popleft()
                same_level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            
            res.append(same_level)
        return res