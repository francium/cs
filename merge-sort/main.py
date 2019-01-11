'''
Input: an array of space separated numbers
Output: sorted array of numbers
'''

from sys import argv


def main(array):
    sorted_array = merge_sort(array)
    print(sorted_array)

def merge_sort(array):
    N = len(array)
    if N == 1: return array
    M = N // 2
    a1 = merge_sort(array[:M])
    a2 = merge_sort(array[M:])

    # Merge two arrays
    sorted_array = []
    I = len(a1)
    J = len(a2)
    i = 0
    j = 0
    # Loop N times since there are a total of N elements
    for _ in range(N):
        v = None
        # If first array exhausted, add from second
        if i == I:
            v = a2[j]
            j += 1
        # Else if second array exhausted, add from first
        elif j == J:
            v = a1[i]
            i += 1
        # Else if next item in second array smaller, add from second
        elif a1[i] >= a2[j]:
            v = a2[j]
            j += 1
        # Else if next item in first array smaller, add from first
        elif a1[i] < a2[j]:
            v = a1[i]
            i += 1

        sorted_array.append(v)
    return sorted_array


array = list(map(int, argv[1:]))
main(array)
