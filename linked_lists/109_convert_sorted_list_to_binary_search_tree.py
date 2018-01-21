# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
        # :TODO fixme
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
    """
    []
    [1]
    [1, 2]
    [1, 2, 3]
    [1, 2, 3, 4]
    [-10, -3, 0, 5, 9]
    :return:
    """
    a = ListNode(-10)
    b = ListNode(-3)
    c = ListNode(0)
    d = ListNode(5)
    e = ListNode(9)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    solution = Solution()
    head = solution.sortedListToBST(a)
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
