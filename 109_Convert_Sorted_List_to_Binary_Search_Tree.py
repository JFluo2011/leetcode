# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next

        def build_tree(values):
            if not values:
                return
            mid = len(values) // 2
            node = TreeNode(values[mid])
            node.left, node.right = build_tree(values[:mid]), build_tree(values[mid+1:])

            return node

        return build_tree(val_list)

    def bottom_up(self, head):
        if head is None:
            return
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next

        def build_tree(start, end):
            if start > end:
                return

            mid = (start + end) // 2
            left = build_tree(start, mid - 1)
            node = TreeNode(val_list[mid])
            node.left, node.right = left, build_tree(mid + 1, end)
            return node

        return build_tree(0, len(val_list) - 1)
