def print_result(lst, attr_name, *args):
    node = dummy = ListNode(None)
    for num in lst:
        node.next = ListNode(num)
        node = node.next

    solution = Solution()
    func = solution.__getattribute__(attr_name)
    if args is not None:
        head = func(dummy.next, *args)
    else:
        head = func(dummy.next)
    results = []
    while head:
        results.append(head.val)
        head = head.next
    print('{}:'.format(attr_name))
    if args is not None:
        print('input: {} {}, output: {}'.format(lst, ' '.join(str(_) for _ in args), results))
    else:
        print('input: {}, output: {}'.format(lst, results))


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # :TODO fixme
        # left = head
        # prev = head
        # for _ in range(m-1):
        #     left = prev
        #     prev = prev.next
        # prev = None
        # cur = prev.next
        # for _ in range(n-m):
        #     cur = prev.next
        #     start = cur.next
        #     cur.next = prev
        #     prev = cur
        #
        # right = cur.next
        # cur.next = prev
        # left.next = start
        # tail.next = right
        # return head


def main():
    test_cases = [
        # ([2], 1, 1),
        ([3, 5], 1, 2),
        # ([4, 2, 1, 3], 1, 1),
        # ([1, 2, 3, 4, 5], 2, 4),
        # ([1, 2, 3, 4, 5], 2, 5),
        ([1, 2, 3, 4, 5, 6, 7, 8], 2, 6),
    ]
    for case in test_cases:
        print_result(case[0], 'reverseBetween', case[1], case[2])


if __name__ == '__main__':
    main()
