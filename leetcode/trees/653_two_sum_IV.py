# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False
        seen = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if k - node.val in seen:
                return True
            seen.add(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return False


def main():
    pass


if __name__ == '__main__':
    main()
