# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        level = 0
        def dfs(node):
            if not node:
                return []
            nonlocal level
            level += 1
            if len(res) < level:
                res.append(node.val)
            dfs(node.right)
            dfs(node.left)
            level -= 1
        dfs(root)
        return res
                
                
