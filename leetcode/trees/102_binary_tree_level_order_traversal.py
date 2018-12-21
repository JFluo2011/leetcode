# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result, stack = [], [root]
        while root and stack:
            result.append([node.val for node in stack])
            stack = [kid for node in stack for kid in (node.left, node.right) if kid]
        return result


def main():
    pass


if __name__ == '__main__':
    main()
