def print_result(lst, attr_name, args=None):
    node = dummy = RandomListNode(None)
    for num in lst:
        node.next = RandomListNode(num)
        node = node.next

    solution = Solution()
    func = solution.__getattribute__(attr_name)
    if args is None:
        head = func(dummy.next)
    else:
        head = func(dummy.next, args)
    results = []
    while head:
        results.append(head.label)
        head = head.next
    print('{}:'.format(attr_name))
    if args is None:
        print('input: {}, output: {}'.format(lst, results))
    else:
        print('input: {} {}, output: {}'.format(lst, args, results))


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        node = head
        # copy node: A->A'->B->B'->C->C'
        while node:
            tmp = RandomListNode(node.label*10)
            tmp.next = node.next
            node.next = tmp
            node = tmp.next
        # set A', B', C' random
        node = head
        while node:
            node.next.random = node.random and node.random.next
            node = node.next.next
        # split list: A->B->C, A'->B'->C'
        node = head
        dummy1 = RandomListNode(0)
        dummy2 = RandomListNode(0)
        l1, l2 = dummy1, dummy2
        while node:
            # node.next = node = copy_.next
            l1.next, l2.next = node, node.next
            l1, l2 = l1.next, l2.next
            node = node.next.next
        else:
            l1.next = None

        # return dummy1.next  # original list
        return dummy2.next


def main():
    test_cases = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
    ]
    for lst in test_cases:
        print_result(lst, 'copyRandomList')


if __name__ == '__main__':
    main()
