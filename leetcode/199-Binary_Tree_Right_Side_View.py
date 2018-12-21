# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        left = self.rightSideView(root.left)
        right = self.rightSideView(root.right)

        return [root.val] + right + left[len(right):]

    def DFS_traverse(self, root):
        def helper(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                helper(node.right, depth+1)
                helper(node.left, depth+1)

        view = []
        helper(root, 0)
        return view

    def Iterative(self, root):
        result = []
        if root:
            stack = [root]
            while stack:
                result.append(stack.pop().val)
                stack = [kid for node in stack for kid in (node.left, node.right) if kid]

        return result

