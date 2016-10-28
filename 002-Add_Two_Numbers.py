class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        list1 = []
        list2 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next

        while l2:
            list2.append(l2.val)
            l2 = l2.next
        result = int(''.join([str(i) for i in list1])[::-1]) + int(''.join([str(i) for i in list2])[::-1])
        return [int(i) for i in str(result)[::-1]]
