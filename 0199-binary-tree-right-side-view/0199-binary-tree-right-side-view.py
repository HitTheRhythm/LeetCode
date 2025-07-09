# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            vals = []
            for i in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
            ans.append(vals[0])
        return ans
                
                
