class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        remaining_roots = set([root])

        def dfs(node):
            if not node:
                return None
            
            res = node
            if node.val in to_delete:
                res = None
                remaining_roots.discard(node)
                if node.left: remaining_roots.add(node.left)
                if node.right: remaining_roots.add(node.right)
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return res
        dfs(root)
        return remaining_roots