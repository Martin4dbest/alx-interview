#!/usr/bin/env python3

def minOperations(n):
    if n == 1:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)
    return n

# Example usage
print(minOperations(9)) # Output: 6

