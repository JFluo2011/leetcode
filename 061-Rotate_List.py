# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        current = head
        length = 1
        while current.next:
            length += 1
            current = current.next

        k = k % length
        current.next = head
        for _ in range(length - k):
            current = current.next

        head = current.next
        current.next = None

        return head


def main():
    """
    []
    0
    [1,2]
    0
    [1,2]
    1
    [1,2]
    2
    [1,2,3]
    4
    [1, 2, 3, 4, 5]
    2
    :return:
    """
    pass


if __name__ == '__main__':
    main()
