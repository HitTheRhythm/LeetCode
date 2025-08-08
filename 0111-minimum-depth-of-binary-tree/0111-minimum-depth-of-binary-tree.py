# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dep = 1
        
        q = deque([root])
        while q:
            sz = len(q)
            for i in range(sz):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return dep
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            dep += 1
        return dep


        
        