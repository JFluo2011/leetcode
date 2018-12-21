# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.get_val_with_depth(result, 0, root)
        return result

    def get_val_with_depth(self, result, depth, node):
        if node is None:
            return
        if len(result) == depth:
            result.append([node.val])
        else:
            result[depth].extend(node.val) if depth % 2 == 0 else result[depth].insert(0, node.val)
        self.get_val_with_depth(result, depth+1, node.left)
        self.get_val_with_depth(result, depth+1, node.right)

    def iterative(self, root):
        result, stack = [], [root]

        while any(stack):
            temp, child = [], []
            while stack:
                node = stack.pop(0)
                if node is None:
                    continue
                temp.append(node.val)
                child.extend([node.left, node.right])
            stack = child
            result.append(temp[::-1]) if len(result) % 2 else result.append(temp)

        return result

    def other(self, root):
        if root is None:
            return []
        result, stack, flag = [], [root], 1

        while stack:
            temp = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
            result.append(temp[::flag])
            flag *= -1

        return result

    def beter(self, root):
        if root is None:
            return []
        import collections
        result, stack, flag = [], collections.deque([root]), 1

        while stack:
            temp = []
            for _ in range(len(stack)):
                node = stack.popleft()
                temp.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
            result.append(temp[::flag])
            flag *= -1

        return result
