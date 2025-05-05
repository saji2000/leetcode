# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minimum = 100000
        maximum = -100000
        if root.left:
            maximum = root.left.val
        
        if root.right:
            minimum = root.right.val

        if not root:
            return True
        
        if root.left and root.right:
            if root.left.val > root.right.val:
                return False
        
        if root.right:
            minimum = min(root.right.val, minimum) 
            return root.right.val > root.val and root.right.val > maximum

        if root.left:
            maximum = max(root.left.val, maximum)
            return root.left.val < root.val and root.left.val < minimum

        left = self.isValidBST(root.left)
        right = self.isValidBST(root.right)
        
        return left and right