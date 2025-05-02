# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maximum):

            if not node:
                return 0

            if node.val >= maximum:
                good = 1
            else:
                good = 0

            
            maximum = max(maximum, node.val)

            return good + dfs(node.right, maximum) + dfs(node.left, maximum)

        return dfs(root, -10000)
            
