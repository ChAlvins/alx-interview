#!/usr/bin/python3
"""Program that performs prime game"""


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    n = max(nums)
    primes_count = [0] * (max(n + 1, 2))

    for i in range(2, int(pow(n, 0.5)) + 1):
        if primes_count[i] == 0:
            for j in range(i * i, n + 1, i):
                primes_count[j] = False

    primes_count[0] = primes_count[1] = 0

    for i in range(2, len(primes_count)):
        primes_count[i] = primes_count[i - 1] + primes_count[i]

    plyr1 = sum(primes_count[n] % 2 == 1 for n in nums)

    if plyr1 * 2 == len(nums):
        return None
    elif plyr1 * 2 > len(nums):
        return "Maria"
    else:
        return "Ben"
