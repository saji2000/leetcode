# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isMatch(self, rootA: Optional[TreeNode], rootB: Optional[TreeNode]):
        if not (rootA and rootB):
            return rootA is rootB
        elif (
            (rootA.val == rootB.val)
            and (self.isMatch(rootA.left, rootB.left))
            and (self.isMatch(rootA.right, rootB.right))
        ):
            return True
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isMatch(root, subRoot):
            return True
        elif not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
