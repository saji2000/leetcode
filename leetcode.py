# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def isSubTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if str(subRoot) in str(root):
            return True
        return False
