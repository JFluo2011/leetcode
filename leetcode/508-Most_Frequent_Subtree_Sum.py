# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        d = {}

        def get_sums(node):
            if node is None:
                return 0
            sums = node.val + get_sums(node.left) + get_sums(node.right)
            d[sums] = d.get(sums, 0) + 1
            return sums

        get_sums(root)
        max_value = max(d.values())
        return [key for key, value in d.items() if value == max_value]
