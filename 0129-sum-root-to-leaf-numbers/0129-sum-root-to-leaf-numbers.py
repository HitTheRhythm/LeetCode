# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.res
    def __init__(self):
        self.path = ''
        self.res = 0
    def traverse(self, node: TreeNode):
        if not node:
            return
        self.path += str(node.val)
        if not node.left and not node.right:
            self.res += int(self.path)
        self.traverse(node.left)
        self.traverse(node.right)
        self.path = self.path[:-1]
