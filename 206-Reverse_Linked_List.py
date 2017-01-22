# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reverse_list = None
        current = head

        while current:
            list_node = current.next
            current.next = reverse_list
            reverse_list = current
            current = list_node

        return reverse_list


def main():
    solution = Solution()
    args = [
        [],
    ]
    for arg in args:
        print(solution.reverseList(arg))


if __name__ == '__main__':
    main()
