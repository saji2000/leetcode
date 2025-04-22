# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        
        if (not root1 and root2) or (root1 and not root2) or (root1.val != root2.val):
            return False
        
        left = self.isSameTree(root1.left, root2.left)
        right = self.isSameTree(root1.right, root2.right)

        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
            
        if self.isSameTree(root, subRoot):
            return True
        
        right = self.isSubtree(root.right, subRoot)
        left = self.isSubtree(root.left, subRoot)

        return left or right

        