# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        prev_head = ListNode(0)
        current = prev_head
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                current = l1
                l1 = l1.next
            else:
                current.next = l2
                current = l2
                l2 = l2.next
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        return prev_head.next


def main():
    """
    []
    []
    [2]
    [1]
    [5, 6, 7]
    [2, 3, 4]
    [-10,-10,-9,-4,1,6,6]
    [-7]
    :return:
    """
    pass


if __name__ == '__main__':
    main()
