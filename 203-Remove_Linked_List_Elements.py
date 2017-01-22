# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev_head = ListNode(0)
        prev_head.next = head
        current = head
        prev = prev_head
        while current:
            while current and current.val == val:
                current = current.next
            prev.next = current
            if current:
                prev = current
                current = current.next

        return prev_head.next


def main():
    """
    []
    1
    [1]
    1
    [1, 2, 6, 3, 4, 5, 6]
    6
    """
    pass


if __name__ == '__main__':
    main()
