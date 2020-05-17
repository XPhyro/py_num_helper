#!/usr/bin/env python3
# Simple number helper.


import math


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or not n % 2:
        return False

    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if not n % i:
            return False

    return True


def prime_factors(n):
    if n < 2:
        return []

    c = 0
    while not n % 2:
        n /= 2
        c += 1

    l = []
    if c:
        l.append((2, c))

    for i in range(3, math.trunc(n) + 1, 2):
        if not is_prime(i):
            continue

        c = 0
        while not n % i:
            n /= i
            c += 1
        if c:
            l.append((i, c))

    return l


def are_twin_primes(s, t):
    return is_prime(s) and is_prime(t) and abs(s - t) == 2


def digit_counts(n):
    n = int(n)
    if n < 1:
        n = -n

    s = str(n)
    l = {}

    for i in range(0, 10):
        l[str(i)] = 0

    for i in s:
        l[i] += 1

    return l
