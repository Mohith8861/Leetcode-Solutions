// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        D = [amount+1] * (amount + 1)
        D[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if (i - coins[j] >= 0):
                    D[i] = min(1 + D[i - coins[j]], D[i])
        return D[amount] if D[amount] != amount + 1 else -1