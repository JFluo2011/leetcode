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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        node = head
        length = 0
        while node:
            node = node.next
            length += 1
        if length < 3:
            return head
        mid = (length + 1) // 2
        # cut list too l1 and l2
        l1 = l2 = head
        prev = head
        while mid > 0:
            prev = l2
            l2 = l2.next
            mid -= 1
        prev.next = None
        # reverse l2
        reverse = None
        while l2 and l2:
            next_ = l2.next
            l2.next = reverse
            reverse = l2
            l2 = next_
        l2 = reverse
        # merge l1 and l2
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next
        return head


def main():
    test_cases = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]
    for lst in test_cases:
        print_result(lst, 'reorderList')


if __name__ == '__main__':
    main()
