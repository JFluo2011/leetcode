# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root

        root.left.val, root.right.val = root.right.val, root.left.val
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
