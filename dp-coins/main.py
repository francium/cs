'''
Input: <target value>, <array of coin values>
    eg: 11 1 2 5 10
Output: Combination of coins from array that sum to target
'''

from sys import argv


def dp_coins_recursive(target, coins):
    '''
    '''
    memo = [None] * (target + 1)

    sorted_coins = sorted(coins)

    combo = []

    def func(target):
        if target == 0: return 0
        # Prevent construction of a solution with negative target
        elif target < 0: return 10e9

        if memo[target] is not None:
            return memo[target]

        u = 10e9
        for coin in sorted_coins:
            u = min(u, func(target - coin)) + 1
        memo[target] = u
        return u

    print(func(target))

def dp_coins_iterative(target, coins):
    memo = [None] * (target + 1)
    memo[0] = 0

    sorted_coins = sorted(coins)

    for i in range(target):
        u = 10e9
        for coin in sorted_coins:
            if (i - coin) < 0: continue
            u = min(u, memo[i - coin] + 1)
        print(u)
        memo[i] = u
    print(memo)




array = list(map(int, argv[2:]))
dp_coins_recursive(int(argv[1]), array)
dp_coins_iterative(int(argv[1]), array)
