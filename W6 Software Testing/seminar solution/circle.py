#!/usr/bin/env python3

from math import pi
import sys


def compute_area(radius):
    if radius < 0.:
        raise ValueError
    return radius ** 2 * pi


def main():
    radius = float(sys.stdin.read().strip())
    area = compute_area(radius)
    sys.stdout.write('{}\n'.format(area))


if __name__ == '__main__':
    main()

