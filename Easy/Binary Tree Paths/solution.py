#Binary Tree Paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
        def binaryTreePaths ( self, root: Optional[TreeNode] ) -> list[str]:
    
                return [ str ( root.val ) + '->' + path
                        for kid in ( root.left, root.right ) if kid
                        for path in self.binaryTreePaths ( kid ) ] or [ str ( root.val ) ]
