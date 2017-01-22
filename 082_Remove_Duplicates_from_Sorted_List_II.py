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
        prev_head = ListNode(0)
        prev_head.next = head
        first = prev_head.next
        second = prev_head.next
        while first and first.next:
            if first.val == first.next.val:
                first.next = first.next.next
            else:
                if second.next != first.next:
                    second.next = first.next
                first = first.next
                second = second.next

        return prev_head.next


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
