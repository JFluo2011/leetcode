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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = prev = node = head
        while node:
            if n > 0:
                n -= 1
            else:
                prev = slow
                slow = slow.next
            fast = fast.next
            node = node.next
        if prev == slow:
            head = prev.next
        prev.next = slow.next
        return head


def main():
    test_cases = [
        ([1], 1),
        ([1, 2], 1),
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 4),
        ([1, 2, 3, 4, 5], 3),
    ]
    for case in test_cases:
        print_result(case[0], 'removeNthFromEnd', case[1])


if __name__ == '__main__':
    main()
