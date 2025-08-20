# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = 1
        res = []
        def dfs(node, order):
            nonlocal res
            if not node:
                return None

            dfs(node.left, order + 1)
            res.append(node.val)
            dfs(node.right, order + 1)
        dfs(root, order)
        return res[k - 1]