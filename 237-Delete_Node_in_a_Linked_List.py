# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node and not node.next:
            return
        node.val = node.next.val
        node.next = node.next.next


def main():
    """
    []
    1
    [1]
    1
    [1, 2, 6, 3, 4, 5, 6]
    6
    """
    pass


if __name__ == '__main__':
    main()
