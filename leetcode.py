# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        queue.append(root)
        ans = []

        while queue:
            length = len(queue)
            right = queue[-1]
            for i in range(length):
                node = queue.popleft()

                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
            if right:
                ans.append(right.val)
        return ans
        
        