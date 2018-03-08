# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        if t.right and t.left is None:
            return str(t.val) + '()' + self.helper(t.right)

        return str(t.val) + self.helper(t.left) + self.helper(t.right)

    def helper(self, t):
        if t is None:
            return ''
        if t.right and t.left is None:
            return '(' + str(t.val) + '()' + self.helper(t.right) + ')'
        return '(' + str(t.val) + self.helper(t.left) + self.helper(t.right) + ')'


def main():
    pass


if __name__ == '__main__':
    main()
