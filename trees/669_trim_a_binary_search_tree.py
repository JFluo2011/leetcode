# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root is None:
            return
        if root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            dummy = TreeNode(root.val)
            dummy.left = self.trimBST(root.left, L, R)
            dummy.right = self.trimBST(root.right, L, R)
            return dummy


def main():
    pass


if __name__ == '__main__':
    main()
