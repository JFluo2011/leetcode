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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return
        # circle the link
        prev = node = head
        length = 0
        while node:
            length += 1
            prev = node
            node = node.next
        prev.next = head
        # find the new head by the position length - (k % length)
        mod = length - (k % length)
        for _ in range(mod):
            prev = prev.next
        head = prev.next
        prev.next = None

        return head


def main():
    test_cases = [
        ([], 3),
        ([1], 3),
        ([1, 2], 3),
        ([1, 2, 3], 3),
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5, 6], 3),
    ]
    for case in test_cases:
        print_result(case[0], 'rotateRight', args=case[1])


if __name__ == '__main__':
    main()
