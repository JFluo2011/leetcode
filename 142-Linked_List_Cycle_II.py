# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        else:
            return None

        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast


def main():
    solution = Solution()
    args = [
        [],
    ]
    for arg in args:
        print(solution.reverseList(arg))


if __name__ == '__main__':
    main()
