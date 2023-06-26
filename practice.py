# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        
        depth_l, depth_r = 0,0
        
    
        if(root.left):
            depth_l = 1 + self.maxDepth(root.left)
        if(root.right):
            depth_r = 1 + self.maxDepth(root.right)

        return max(depth_l, depth_r)

