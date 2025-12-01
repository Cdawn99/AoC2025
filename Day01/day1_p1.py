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
        val = sign * int(rot[1:])
        dial = (dial + val) % 100
        if dial == 0:
            password += 1

    print(f'Password is: {password}')
