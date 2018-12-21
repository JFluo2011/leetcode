def print_result(lst, attr_name, args=None):
    node = dummy = ListNode(None)
    for num in lst:
        node.next = ListNode(num)
        node = node.next

    solution = Solution()
    func = solution.__getattribute__(attr_name)
    if args is None:
        head = func(dummy.next)
    else:
        head = func(dummy.next, args)
    # results = []
    # while head:
    #     results.append(head.val)
    #     head = head.next
    # print('{}:'.format(attr_name))
    # if args is None:
    #     print('input: {}, output: {}'.format(lst, results))
    # else:
    #     print('input: {} {}, output: {}'.format(lst, args, results))


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        slow = head
        fast = head
        prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        prev.next = None
        left = head
        if slow == left:
            left = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
        return root


def main():
    test_cases = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [-10, -3, 0, 5, 9],
    ]
    for lst in test_cases:
        print_result(lst, 'sortedListToBST')


if __name__ == '__main__':
    main()
