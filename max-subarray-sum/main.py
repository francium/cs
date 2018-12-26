'''
Given an array of n integers, find the max subarray sub (the largest possible sum of
numbers in a contiguous region in the array)
See: Competitive Programmer's Handbook p.23

Input: an array of space separated numbers
Output: max sum of all subarrays of the array of numbers
'''

from sys import argv


def mainO3(array):
    '''O(n^3)'''
    N = len(array)
    maxsum = -10e9
    # Go over all starting positions
    for i in range(0, N):
        # Go over all ending positions
        for j in range(i, N):
            newsum = 0
            # Sum all numbers between starting and ending position
            for k in range(i, j + 1):
                newsum += array[k]
            maxsum = max(newsum, maxsum)
    print(maxsum)


def mainO2(array):
    '''O(n^2)'''
    N = len(array)
    maxsum = -10e9
    # Go over all starting positions
    for i in range(0, N):
        # Sum of the subarray starting at position i
        newsum = 0
        # Go over all ending positions
        for j in range(i, N):
            # Sum of local subarray from ith position to jth position in array
            newsum = newsum + array[j]
            # Take bigger of the two: local subarray from i to j or the current global
            # best
            maxsum = max(newsum, maxsum)
    print(maxsum)

def mainOn(array):
    '''
    O(n)
    Kadene's algorithm
    Make a single pass through the array keeping track of the best subarray at ends at
    current position.
    '''
    N = len(array)
    # Global max subarray sum.
    maxsum = -10e9
    # Local max subarray sum.
    sum_ = -10e9
    for i in range(0, N):
        # If it's better to start a new subarray instead of continuing the previous
        # subarray, set local subarray sum to current element only. Otherwise, local
        # subarray sum is sub of previous subarray's sum and current element.
        sum_ = max(array[i], sum_ + array[i])

        # It's possible there are multiple locally optimal subarray. This algorithm will
        # only keep track of the current best locally optimal subarray. So this variable
        # stored the best overall subarray sum.
        maxsum = max(sum_, maxsum)
    print(maxsum)


def main(array):
    mainO3(array)
    mainO2(array)
    mainOn(array)


array = list(map(int, argv[1:]))
main(array)
