# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root)
        return root

    def helper(self, node, total=0):
        if node is None:
            return total
        total = self.helper(node.right, total)
        node.val += total
        total = node.val
        total = self.helper(node.left, total)
        return total


def main():
    pass


if __name__ == '__main__':
    main()
