import sys
import math


def is_invalid_id(n):
    nlen = int(math.log10(n)) + 1
    if nlen % 2 != 0:
        return False
    n1, n2 = divmod(n, 10**(nlen//2))
    return n1 == n2


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: python3 {sys.argv[0]} <input.txt>')
        exit(0)

    with open(sys.argv[1], 'r') as f:
        contents = f.read().strip().split(',')

    id_sum = 0
    for rng in contents:
        rng = rng.split('-')
        if len(rng[0]) % 2 != 0 and len(rng[1]) % 2 != 0 and len(rng[0]) == len(rng[1]):
            continue
        for i in range(int(rng[0]), int(rng[1]) + 1):
            if is_invalid_id(i):
                id_sum += i

    print(f'Sum of invalid ids: {id_sum}')
