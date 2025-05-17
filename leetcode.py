# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mySet = set()

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(node):
            if not node:
                return
            self.mySet.add(node.val)

            traverse(node.left)
            traverse(node.right)
        
        traverse(root)

        for i in range(k):
            minimum = min(self.mySet)
            self.mySet.remove(minimum)
        
        return minimum
        