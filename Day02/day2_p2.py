import sys
import math


def is_made_of_repeated_seq_of_len(x, n):
    x, seq = divmod(x, 10**n)
    while x % 10**n == seq:
        x //= 10**n
    return x == 0


def is_invalid_id(x):
    xlen = int(math.log10(x)) + 1
    for i in range(xlen // 2):
        if is_made_of_repeated_seq_of_len(x, i):
            return True
    return False


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: python3 {sys.argv[0]} <input.txt>')
        exit(0)

    with open(sys.argv[1], 'r') as f:
        contents = f.read().strip().split(',')

    ranges = []
    for rng in contents:
        rng = rng.split('-')
        ranges.append((int(rng[0]), int(rng[1]) + 1))

    id_sum = 0
    for rng in ranges:
        for i in range(*rng):
            if is_invalid_id(i):
                id_sum += i

    print(f'Sum of invalid ids: {id_sum}')
