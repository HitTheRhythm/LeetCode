# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            sz = len(q)
            arr = []
            for i in range(sz):
                node = q.popleft()
                arr.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(arr)
        return ans
         



