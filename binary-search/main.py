'''
Input: element to search for, an array of space separated numbers
    eg: <4 2 3 -5 3 1> will search for the element '4' in the array '2 3 -5 3 1'
Output: True or false depending on if the element is in the array
'''

from sys import argv


def binary_search(el, array):
    N = len(array)
    l = 0
    r = N - 1
    # After each iteration either the l or r get moved to +/-1 places around the floored
    # middle position. Eventually they'll either cross over and l will become larger than
    # r (meaning the target is not in the array) or they will settle on the same position
    # and that position is the target.
    while l <= r:
        m = (l + r) // 2
        if array[m] == el: return True
        elif el < array[m]: r = m - 1
        elif el > array[m]: l = m + 1
    return False


def bottenbruch_binary_search(el, array):
    '''
    This algorithm leaves out the extra comparison during each iteration to check if the
    middle element is the target. But it does however use more iterations on average
    See: https://en.wikipedia.org/wiki/Binary_search_algorithm#Alternative_procedure
    '''
    N = len(array)
    l = 0
    r = N - 1
    # This approach does not check if the middle element is the target until the
    # iterations are complete and the l and r have gotten to the same position or have
    # crossed over.
    while l != r and l <= r:
        m = (l + r) // 2
        if el < array[m]: r = m - 1
        else:             l = m + 1
    # If the elements have not crossed over and the target is at this final position, then
    # the search is successful, otherwise l and r crossed over and the target was not
    # found.
    return l == r and el == array[l]


def main(el, array):
    sorted_array = sorted(array)
    print(binary_search(el, sorted_array))
    print(bottenbruch_binary_search(el, sorted_array))


array = list(map(int, argv[2:]))
main(int(argv[1]), array)
