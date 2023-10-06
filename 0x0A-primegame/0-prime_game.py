#!/usr/bin/python3

def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes_up_to_n(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def calculate_winner(primes_left):
        if not primes_left:
            return "Ben"
        return "Maria" if len(primes_left) % 2 == 1 else "Ben"

    overall_winner = None
    for n in nums:
        primes_left = get_primes_up_to_n(n)
        round_winner = calculate_winner(primes_left)
        if overall_winner is None:
            overall_winner = round_winner
        elif round_winner is not None:
            if overall_winner != round_winner:
                overall_winner = None

    return overall_winner
