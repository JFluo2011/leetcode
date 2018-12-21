# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        48ms
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left is not None and root.right is not None:
                left, right = root.left, root.right
                root.right = root.left
                while left:
                    if left.left is None and left.right is None:
                        break
                    left = left.right if left.right else left.left
                left.right = right
            elif root.left is None and root.right is None:
                return
            elif root.left is None:
                pass
            else:
                root.right = root.left
            root.left = None
            root = root.right

    def faster(self, root):
        """
        45ms
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left is not None and root.right is not None:
                left, right = root.left, root.right
                root.right = root.left
                root.left = None
                while left:
                    if left.left is None and left.right is None:
                        break
                    left = left.right if left.right else left.left
                left.right = right
                root = root.right
            elif root.left is None and root.right is None:
                return
            elif root.left is None:
                root = root.right
            else:
                root.right = root.left
                root.left = None
                root = root.right

    def dfs(self, root):
        prev = TreeNode(-1)
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            prev.right = node
            prev.left = None
            stack.append(node.right)
            stack.append(node.left)
            prev = prev.right

    def recursive(self, root):
        if root is None:
            return

        left, right = root.left, root.right
        if left is not None:
            root.right, root.left = left, None
            while left.right is not None:
                left = left.right
            left.right = right
        self.flatten(root.right)

    def other_recursive(self, root):
        if root is None:
            return
        left, right = root.left, root.right
        self.other_recursive(right)
        if left is None:
            return
        self.other_recursive(left)
        root.right, root.left = left, None
        while left.right is not None:
            left = left.right
        left.right = right
