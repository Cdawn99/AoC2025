import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 day1.py <input.txt>')
        exit(0)

    with open(sys.argv[1], 'r') as f:
        rotations = f.read().strip().splitlines()

    dial = 50
    password = 0
    for rot in rotations:
        sign = -1 if rot[0] == 'L' else 1
        val = int(rot[1:])
        if val >= 100:
            inc, val = divmod(val, 100)
            password += inc
        prev_was_zero = dial == 0
        dial += sign * val
        if not prev_was_zero and (dial <= 0 or 100 <= dial):
            password += 1
        dial %= 100
        # print(f'{rot}: {password}')

    print(f'Password is: {password}')
