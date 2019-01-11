'''
Input: <target value>, <array of coin values>
    eg: 11 1 2 5 10
Output: Combination of coins from array that sum to target
'''

from sys import argv


def main(target, coins):
    '''
    This solution takes a greedy approach and selects the highest coin that's less than or
    equal to the remaining target value
    '''
    t = target
    sorted_coins = sorted(coins)
    combo = []
    while t > 0:
        highest = sorted_coins[-1]
        if highest <= t:
            t -= highest
            combo.append(highest)
        else:
            sorted_coins.pop()
    print(combo)


array = list(map(int, argv[2:]))
main(int(argv[1]), array)
