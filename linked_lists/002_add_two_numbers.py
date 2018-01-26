def print_result(lst, lst2, attr_name):
    node = dummy = ListNode(None)
    for num in lst:
        node.next = ListNode(num)
        node = node.next
    node2 = dummy2 = ListNode(None)
    for num in lst2:
        node2.next = ListNode(num)
        node2 = node2.next

    solution = Solution()
    func = solution.__getattribute__(attr_name)
    head = func(dummy.next, dummy2.next)
    results = []
    while head:
        results.append(head.val)
        head = head.next
    print('{}:'.format(attr_name))
    print('input: {} {}, output: {}'.format(lst, lst2, results))


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lst, num = [node for node in (l1, l2) if node], 0
        dummy = head = ListNode(None)
        while lst or num:
            num += sum(node.val for node in lst)
            head.next = ListNode(num % 10)
            head = head.next
            num //= 10
            lst = [node.next for node in lst if node.next]

        return dummy.next


def main():
    test_cases = [
        ([], []),
        ([2, 4, 3], [5, 6, 4]),
        ([2, 4, 3], [5, 6, 6]),
        ([5, 4, 3], [5, 6, 6]),
    ]
    for case in test_cases:
        print_result(case[0], case[1], 'addTwoNumbers')


if __name__ == '__main__':
    main()
