# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        q = deque([root])
        level = 1
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if level == 1 and node.val % 2 == 0: return False
                if level == -1 and node.val % 2 == 1: return False
                if i < size - 1:
                    if level == 1 and node.val >= q[0].val: return False
                    if level == -1 and node.val <= q[0].val: return False

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level = -level
        return True