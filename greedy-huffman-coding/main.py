'''
Input:
Output:
'''

from sys import argv


def main(target, coins):
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
