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
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # TODO fixme


def main():
    test_cases = [
        [],
        [5, 2, 3, 4, 1],
        [1, 2, 3, 4, 5],
    ]
    for lst in test_cases:
        print_result(lst, 'deleteDuplicates')


if __name__ == '__main__':
    main()
