'''
Input: an array of space separated numbers
Output: sorted array of numbers
'''

from sys import argv


def main(array):
    N = len(array)
    # From N - 1 to 1 (highest index to second lowest)
    #   In first loop, shrink the working array from the right side. Since each iteration
    #   will push the largest element to the right side, we shrink the array since that
    #   element is in its final position.
    for i in range(N - 1, 0, -1):
        # From 0 to i - 1 (lowest index to second highest index up to position i)
        #  i - 1 b/c we want to be able to reference the current element and the next
        #  element (which isn't possible if we go up to i)
        for j in range(0, i):
            print(i, j, N)
            if (array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    print(array)


array = list(map(int, argv[1:]))
main(array)
