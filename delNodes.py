def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        remaining_roots = set([root])

        def dfs(node):
            if not node:
                return
            
            curr = node 

            if curr.val in to_delete:
                remaining_roots.discard(curr)
                curr = None
                if node.left: remaining_roots.add(node.left)
                if node.right: remaining_roots.add(node.right)
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return curr

        dfs(root)
        return list(remaining_roots)
                