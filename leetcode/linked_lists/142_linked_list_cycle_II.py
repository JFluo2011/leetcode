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
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break
        else:
            return None

        while slow != head:
            slow = slow.next
            head = head.next
        return head


def main():
    test_cases = [
        # [],
        # [1],
        # [1, 2],
        # [1, 2, 3],
        # [1, 2, 3, 4],
        [1, 3, 2, 5, 4, 2],
    ]
    for case in test_cases:
        print_result(case, 'detectCycle')


if __name__ == '__main__':
    main()
