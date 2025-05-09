"""
Prime Sieve using Asyncio

This program uses the Prime Sieve algorithm to calculate all prime numbers
up to a given limit, using asyncio for improved performance.

Author: [Your Name]
Date: [Date]
License: [License, if applicable]

PEP 8 Compliance:
- 4 spaces per indentation level
- Maximum line length of 79 characters
"""

import asyncio
import time


async def prime_sieve(limit):
    """
    Calculate all prime numbers up to the given limit using the Prime Sieve
    algorithm.

    Args:
        limit (int): The upper limit for the prime numbers to calculate.

    Returns:
        list: A list of all prime numbers up to the given limit.
    """
    is_prime = [True] * (limit + 1)
    primes = []

    for n in range(2, limit + 1):
        if is_prime[n]:
            primes.append(n)
            for i in range(n * n, limit + 1, n):
                is_prime[i] = False

    return primes


async def main():
    """
    The primary function of the program.
    """
    # Define the limit for prime numbers
    limit = 100000000

    # Record the start time
    start_time = time.perf_counter()

    # Run the Prime Sieve algorithm
    primes = await prime_sieve(limit)

    # Record the end time
    end_time = time.perf_counter()

    # Print the results
    print(f"Number of primes: {len(primes)}")
    print(f"Execution time: {end_time - start_time:.3f} seconds")


if __name__ == '__main__':
    asyncio.run(main())
