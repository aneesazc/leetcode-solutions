def get_prime_factors(N):
    prime_factors = []  # List to store prime factors

    # Divide by 2 as many times as possible
    while N % 2 == 0:
        prime_factors.append(2)
        N //= 2  # Divide N by 2

    # Check for odd divisors starting from 3, up to the square root of N
    for i in range(3, int(N**0.5) + 1, 2):
        while N % i == 0:  # Divide by i as many times as possible
            prime_factors.append(i)
            N //= i

    # If there's any remaining prime factor larger than sqrt(N)
    if N > 2:
        prime_factors.append(N)

    return prime_factors

# Example usage:
print(get_prime_factors(56))  # Expected: [2, 2, 2, 7]
print(get_prime_factors(48))  # Expected: [2, 2, 2, 2, 3]
print(get_prime_factors(37))  # Expected: [37] (since it's a prime number)



import math


def prime_factors(n):
    res = []
    while n % 2 == 0:
        n = n // 2
        res.append(2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n = n // i
            res.append(i)
    if n > 2:
        res.append(n)
        
    return res


'''
Divide N by two as many times as you can do so evenly (no remainder). For each division, append a 2 to the list of prime factors
At this point, N must be odd. Start a loop that iterates over all odd numbers from 3 to the square root of N inclusive. Use math.sqrt().
For each number i, if N can be divided evenly by i, then divide N by i and append i to the list. Repeat this (nested loop) until i can't divide evenly into N, then move on to the next i
If N is still greater than 2 after that loop, it must still be prime, so just append it to the list.
Return the list of primes
'''
