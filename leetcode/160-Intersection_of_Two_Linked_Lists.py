# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p_a = headA
        p_b = headB
        length_a = 0
        length_b = 0
        while p_a:
            p_a = p_a.next
            length_a += 1

        while p_b:
            p_b = p_b.next
            length_b += 1
        p_longer, p_shorter = (headA, headB) if length_a >= length_b else (headB, headA)

        for _ in range(abs(length_b - length_a)):
            p_longer = p_longer.next
        for _ in range(min(length_b, length_a)):
            if p_longer == p_shorter:
                return p_longer
            else:
                p_longer = p_longer.next
                p_shorter = p_shorter.next


def main():
    pass


if __name__ == '__main__':
    main()
