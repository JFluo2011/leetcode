# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

    def Iterative(self, root):
        result, stack = [], [root]

        while stack:
            node = stack.pop()
            if node is not None:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return result
