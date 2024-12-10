#!/usr/bin/python3
"""This module contains a function that Determines the winner of the prime game"""
def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): A list of integers representing the upper limit (n) for each round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben").
        None: If the winner cannot be determined (tie).
    """
    if x < 1 or not nums:
        return None  # Return None if no rounds or nums list is empty.

    # Find the maximum number in nums to optimize prime computation.
    max_num = max(nums)

    # Step 1: Precompute primes up to max_num using the Sieve of Eratosthenes.
    # Create a list where True represents a prime number.
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers.
    for i in range(2, int(max_num**0.5) + 1):  # Iterate up to the square root of max_num.
        if primes[i]:
            # Mark multiples of i as non-prime.
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Step 2: Precompute the cumulative count of primes up to each index.
    # This allows O(1) access to the number of primes up to any n.
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Step 3: Simulate the game for each round.
    # Track the number of rounds won by Maria and Ben.
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the number of moves by counting primes up to n.
        moves = prime_count[n]
        if moves % 2 == 1:
            maria_wins += 1  # Maria wins if the total moves are odd.
        else:
            ben_wins += 1  # Ben wins if the total moves are even.

    # Step 4: Determine the overall winner.
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # Return None if the game ends in a tie.