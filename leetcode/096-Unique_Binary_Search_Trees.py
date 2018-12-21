class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0] * (n + 1)
        result[0] = 1

        for i in range(n+1):
            for j in range(i):
                result[i] += result[j] * result[i-j-1]

        return result[n]

    def recursive(self, n):
        result = [1] * 2 + [0] * (n - 1)

        def count_trees(num):
            if (num == 0) or (num == 1):
                return 1

            if result[num] != 0:
                return result[num]

            for i in range(num):
                result[num] += count_trees(i) * count_trees(num - i - 1)
            return result[num]

        count_trees(n)
        return result[n]
