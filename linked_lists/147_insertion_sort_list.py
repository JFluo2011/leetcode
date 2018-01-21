# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # :TODO fixme
        # result_node = node = ListNode(head.val)
        # head = head.next
        # while head:
        #     tmp = prev = node
        #     while tmp and tmp.next:
        #
        #         prev = tmp
        #         tmp = tmp.next
        #     if tmp == node:
        #         new_node = ListNode(head.val)
        #         new_node.next = node
        #         node = new_node
        #     else:
        #         if not tmp:
        #             tmp = prev
        #         tmp.next = ListNode(head.val)
        #     head = head.next
        # return result_node


def main():
    """
    []
    [1]
    [1, 2]
    [1, 2, 3]
    [1, 2, 3, 4]
    [1, 3, 2, 5, 4]
    :return:
    """
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(2)
    d = ListNode(5)
    e = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    solution = Solution()
    head = solution.insertionSortList(a)
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
