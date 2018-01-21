# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = prev = node = head
        while node:
            if n > 0:
                n -= 1
            else:
                prev = slow
                slow = slow.next
            fast = fast.next
            node = node.next
        if prev == slow:
            head = prev.next
        prev.next = slow.next
        return head


def main():
    """
    []
    [1]
    [1, 2]
    [1, 2, 3]
    [1, 2, 3, 4]
    [1, 2, 3, 4, 5]
    :return:
    """
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    solution = Solution()
    head = solution.removeNthFromEnd(a, 2)
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
