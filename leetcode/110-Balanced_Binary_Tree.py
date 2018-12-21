# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        def max_depth(node):
            if node is None:
                return 0

            return 1 + max(max_depth(node.left), max_depth(node.right))

        left_depth = max_depth(root.left)
        right_depth = max_depth(root.right)

        if abs(left_depth - right_depth) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depthAndBalan(self, root):
        if root is None:
            return 0, True
        leftDep, leftBal = self.depthAndBalan(root.left)
        rightDep, rightBal = self.depthAndBalan(root.right)
        curBal = abs(leftDep - rightDep) <= 1
        return max(leftDep, rightDep) + 1, leftBal and rightBal and curBal

    def better(self, root):
        return self.depthAndBalan(root)[1]
