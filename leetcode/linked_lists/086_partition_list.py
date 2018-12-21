def print_result(lst, attr_name, args=None):
    node = dummy = ListNode(None)
    for num in lst:
        node.next = ListNode(num)
        node = node.next

    solution = Solution()
    func = solution.__getattribute__(attr_name)
    if args is None:
        head = func(dummy.next)
    else:
        head = func(dummy.next, args)
    results = []
    while head:
        results.append(head.val)
        head = head.next
    print('{}:'.format(attr_name))
    if args is None:
        print('input: {}, output: {}'.format(lst, results))
    else:
        print('input: {} {}, output: {}'.format(lst, args, results))


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next


def main():
    test_cases = [
        # ([], 1),
        # ([1], 0),
        # ([1], 2),
        # ([1, 2], 1),
        # ([2, 1], 2),
        # ([2, 1], 1),
        # ([2, 1], 0),
        # ([1, 2, 3], 1),
        # ([4, 2, 1, 3], 2),
        ([1, 4, 3, 2, 5, 2], 3),
    ]
    for case in test_cases:
        print_result(case[0], 'partition', case[1])


if __name__ == '__main__':
    main()
