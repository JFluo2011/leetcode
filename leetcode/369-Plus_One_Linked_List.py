# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def plusOne(self, head):
        if not head.next:
            head.val += 1
            return head

        return self.plusOne(head.next)


def main():
    pass


if __name__ == '__main__':
    main()
