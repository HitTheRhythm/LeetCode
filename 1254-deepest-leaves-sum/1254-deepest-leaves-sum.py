# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        while q:
            size = len(q)
            s = 0
            for _ in range(size):
                node = q.popleft()
                s += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return s
