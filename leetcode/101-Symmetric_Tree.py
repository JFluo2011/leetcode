# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        72ms
        """
        pre_list = []
        in_list = []
        post_list = []

        def in_order(node):
            if node is None:
                return
            in_order(node.left)
            in_list.append(node.val)
            in_order(node.right)

        def pre_order(node):
            if node is None:
                return
            pre_list.append(node.val)
            pre_order(node.left)
            pre_order(node.right)

        def post_order(node):
            if node is None:
                return
            post_order(node.left)
            post_order(node.right)
            post_list.append(node.val)

        in_order(root)
        if in_list != in_list[::-1]:
            return False
        pre_order(root)
        post_order(root)
        return pre_list == post_list[::-1]

    def other_with_recursively(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        49ms
        """
        def isSym(L, R):
            if not L and not R:
                return True
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False

        return isSym(root, root)

    def other_with_iteratively(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        49ms
        """
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True

