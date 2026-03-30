def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(limit):
    return [n for n in range(2, limit) if is_prime(n)]

# Example usage
primes = get_primes(100)
print(primes)