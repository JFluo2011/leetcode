class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins_count = [0] + [-1] * amount
        coins_used = [0] + [-1] * amount
        for i in range(amount):
            if coins_count[i] < 0:
                continue
            coin_use = -1
            for c in coins:
                if i + c > amount:
                    continue
                if (coins_count[i + c] < 0) or (coins_count[i + c] > coins_count[i] + 1):
                    coins_count[i + c] = coins_count[i] + 1
                    coin_use = c
            coins_used = coin_use
        # return coins_count[amount]
        return coins_count, coins_used

    def rec_coin_dynam(self, coins, amount, coins_count):
        if amount in coins:
            coins_count[amount] = 1
            return 1
        elif (coins_count[amount] > 0) and (coins_count[amount] < 5):
            return coins_count[amount]

        min_count = amount
        for coin in [c for c in coins if c <= amount]:
            count = self.rec_coin_dynam(coins, amount-coin, coins_count) + 1
            if count < min_count:
                min_count = count
                coins_count[amount] = min_count

        return min_count

    def better(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [-1] * amount
        for x in range(amount):
            if dp[x] < 0:
                continue
            for c in coins:
                if x + c > amount:
                    continue
                # print("**************************")
                # print(x, c, dp)
                if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
                    dp[x + c] = dp[x] + 1
                # print(x, c, dp)
                # print("**************************")
        return dp[amount]

    def _get_change_making_matrix(self, set_of_coins, r):
        m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
        for i in range(r + 1):
            m[0][i] = i
        return m

    def change_making(self, coins, n):
        """
        This function assumes that all coins are available infinitely.
        n is the number that we need to obtain with the fewest number of coins.
        coins is a list or tuple with the available denominations.
        """
        m = self._get_change_making_matrix(coins, n)
        for c in range(1, len(coins) + 1):
            for r in range(1, n + 1):
                # Just use the coin coins[c - 1].
                if coins[c - 1] == r:
                    m[c][r] = 1
                # coins[c - 1] cannot be included.
                # We use the previous solution for making r,
                # excluding coins[c - 1].
                elif coins[c - 1] > r:
                    m[c][r] = m[c - 1][r]
                # We can use coins[c - 1].
                # We need to decide which one of the following solutions is the best:
                # 1. Using the previous solution for making r (without using coins[c - 1]).
                # 2. Using the previous solution for
                # making r - coins[c - 1] (without using coins[c - 1]) plus this 1 extra coin.
                else:
                    m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])

        return m[-1][-1]


def main():
    solution = Solution()
    args = [
        # ([1], 0),
        ([2], 5),
        # ([2, 3], 7),
        # ([3, 5], 7),
        # ([2, 3], 9),
        # ([1, 2, 5], 11),
        # # ([1, 5, 10], 11),
        # ([186, 419, 83, 408], 6249),
        # ([83, 186, 419, 408], 6249),
    ]
    for arg in args:
        # coins_count, coins_used = solution.coinChange(*arg)
        # print(coins_count)
        # print(coins_count[arg[1]])
        # print(solution.dpMakeChange(*arg))
        # print(solution.better(*arg))
        print(solution.change_making(*arg))
        # coins_count = [0] + [arg[1]] * arg[1]
        # result = solution.rec_coin_dynam(*arg, coins_count)
        # if result > arg[1]:
        #     print(-1)
        # else:
        #     print(result)
        # print(coins_count)


if __name__ == '__main__':
    main()
