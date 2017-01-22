# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return []
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        if length < n:
            return []
        prev_head = ListNode(0)
        prev_head.next = head
        current = prev_head
        for _ in range(length - n):
            current = current.next

        current.next = current.next.next

        return prev_head.next


def main():
    """
    [1]
    1
    [1, 2, 3, 4, 5]
    5
    [1,2]
    2
    :return:
    """
    pass


if __name__ == '__main__':
    main()
