class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []

        for i in preorder.split(','):
            stack.append(i)

            while (len(stack) >= 3) and stack[-2:] == ['#', '#']:
                stack[-3:-1] = []

        return True if (stack == ['#']) else False

    def other(self, preorder):
        diff = 1
        for item in preorder.split(','):
            diff -= 1
            if item != '#':
                diff += 2

        return diff == 0

    def other_with_re(self, preorder):
        import re
        while re.search(r'[0-9]+,#,#', preorder):
            preorder = re.sub(r'[0-9]+,#,#', '#', preorder)

        return preorder == '#'
