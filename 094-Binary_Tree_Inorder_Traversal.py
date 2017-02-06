# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def Iterative(self, root):
        result, stack = [], []

        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return result

            node = stack.pop()
            result.append(node.val)
            root = node.right
