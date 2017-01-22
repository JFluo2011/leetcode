# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        first = head
        second = head
        prev = head
        while m > 1:
            prev = first
            first = first.next
            m -= 1

        while n > 0:
            second = second.next
            n -= 1

        reverse_list = None
        temp = first
        while temp != second:
            node = temp.next
            temp.next = reverse_list
            reverse_list = temp
            temp = node

        if first != head:
            prev.next = reverse_list
        else:
            head = reverse_list
        if second:
            first.next = second
        return head

    def better(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        prev_head = ListNode(0)
        prev_head.next = head
        p = prev_head

        for _ in range(m - 1):
            p = p.next

        current = p.next
        for _ in range(n - m):
            tmp = current.next
            current.next = tmp.next
            tmp.next = p.next
            p.next = tmp

        return prev_head.next


def main():
    solution = Solution()
    '''
    [1, 2, 3, 4, 5, 6]
    2
    4

    [1, 2, 3, 4, 5, 6]
    2
    6

    [1, 2, 3, 4, 5, 6]
    0
    6
    '''
    print(solution.reverseBetween(ListNode(5), 1, 1))


if __name__ == '__main__':
    main()
