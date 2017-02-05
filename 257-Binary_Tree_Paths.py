# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []

        return [str(root.val) + '->' + path
                for kid in (root.left, root.right)
                for path in self.binaryTreePaths(kid)] or [str(root.val)]

    def Iterative(self, root):
        if root is None:
            return []
        result, stack = [], [(root, '')]

        while stack:
            node, path = stack.pop()
            if node.left is None and node.right is None:
                result.append(path + str(node.val))
            if node.right:
                stack.append((node.right, path + str(node.val) + '->'))
            if node.left:
                stack.append((node.left, path + str(node.val) + '->'))

        return result

