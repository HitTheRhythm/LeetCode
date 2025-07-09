# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = deque([root])
        odd = False
        while q:
            nodes = []
            for _  in range(len(q)):
                node = q.popleft()
                nodes.append(node)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if odd:
                left,right = 0, len(nodes) -1
                while left < right:
                    nodes[left].val, nodes[right].val = nodes[right].val, nodes[left].val
                    left += 1
                    right -= 1
            odd = not odd
        return root
