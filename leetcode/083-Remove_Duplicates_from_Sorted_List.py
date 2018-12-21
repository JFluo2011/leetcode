# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first = head
        while first and first.next:
            if first.val == first.next.val:
                first.next = first.next.next
            else:
                first = first.next

        return head


def main():
    """
    []
    [1, 1, 2, 2]
    [1, 1, 1, 1, 2, 3, 3]
    :return:
    """
    pass


if __name__ == '__main__':
    main()
