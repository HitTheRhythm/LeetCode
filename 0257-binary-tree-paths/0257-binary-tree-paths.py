# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.construct(root)
        return self.res

    def __init__(self):
        self.res = []
        self.path = []

    def construct(self, node: TreeNode):
        if not node:
            return
        if not node.left and not node.right:
            self.path.append(str(node.val))
            self.res.append("->".join(self.path))
            self.path.pop()
        
        self.path.append(str(node.val))
        self.construct(node.left)
        self.construct(node.right)
        self.path.pop()
            
            