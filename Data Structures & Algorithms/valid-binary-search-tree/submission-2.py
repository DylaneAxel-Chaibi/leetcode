# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float('-inf'), float('inf'))
    
    def valid(self, root: Optional[TreeNode], l: int, r: int) -> bool:
        if not root :
            return True
        if root.val <= l or root.val >= r :
            return False
        return self.valid(root.left, l, root.val) and self.valid(root.right, root.val, r)
