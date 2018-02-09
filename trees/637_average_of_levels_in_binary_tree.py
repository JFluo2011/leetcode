# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        results = []
        stack = [root]
        while stack:
            results.append(sum(node.val for node in stack) / len(stack))
            stack = [child for node in stack for child in (node.left, node.right) if child]
        return results


def main():
    pass


if __name__ == '__main__':
    main()
