# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, minimum, maximum):
            if not node:
                return True

            if node.val <= minimum or node.val >= maximum:
                return False
    
            right = dfs(node.right, node.val, maximum)
            left = dfs(node.left, minimum, node.val)
            
            return left and right
        
        return dfs(root, -math.inf, math.inf)
        
            
        