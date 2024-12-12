#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_num + 1, i):
                sieve[j] = False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(1 for i in range(2, n + 1) if sieve[i])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None

