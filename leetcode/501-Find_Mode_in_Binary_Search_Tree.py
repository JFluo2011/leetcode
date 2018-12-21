# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        d = {}

        def count(node):
            if node:
                d[node.val] = d.get(node.val, 0) + 1
                count(node.left)
                count(node.right)

        count(root)
        max_val = max(d.values())
        return [key for key, value in d.items() if value == max_val]

    def other(self, root):
        if root is None:
            return []
        d = collections.Counter()

        def count_val(node):
            if node:
                d[node.val] += 1
                count_val(node.left)
                count_val(node.right)

        count_val(root)
        max_val = max(d.itervalues())
        return [key for key, value in d.iteritems() if value == max_val]

    def Iterative(self, root):
        if root is None:
            return []
        d = collections.Counter()
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                d[node.val] += 1
                stack.append(node.left)
                stack.append(node.right)

        max_val = max(d.itervalues())
        return [key for key, value in d.iteritems() if value == max_val]