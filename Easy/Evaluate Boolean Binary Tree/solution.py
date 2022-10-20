#Evaluate Boolean Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     	def __init__(self, val=0, left=None, right=None):
#         	self.val = val
#         	self.left = left
#         	self.right = right

class Solution:

    	def evaluateTree ( self, root: Optional[TreeNode] ) -> bool:
        
		if root.left == None and root.right == None:    #leaf node
			return True if root.val == 1 else False
		
		left = self.evaluateTree ( root.left )
		right = self.evaluateTree ( root.right )
		
		if root.val == 2:               #if node.val is 'OR'
			res = left or right
		if root.val == 3:               #if node.val is 'AND'
			res = left and right
		
		return res
