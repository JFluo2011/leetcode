# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd = head
        tmp = even = head.next
        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        odd.next = tmp
        return head


def main():
    """
    []
    [1]
    [1, 2]
    [1, 2, 3]
    [1,2,3,4,5,6,7,8]
    :return:
    """
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    g = ListNode(7)
    h = ListNode(8)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h

    solution = Solution()
    head = solution.oddEvenList(a)
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
