def atoi(string):
    ZERO = ord('0')

    val = 0
    power = 1
    for c in string[::-1]:
        val += power * (ord(c) - ZERO)
        power *= 10
    return val, type(val)


if __name__ == '__main__':
    print(atoi(input('enter a number> ')))
