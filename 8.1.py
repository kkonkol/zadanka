import random

def is_prime(n, k=5):  
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    def miller_rabin(a, d, n, r):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if not miller_rabin(a, d, n, r):
            return False

    return True

def generate_prime(n):
    while True:
        s = random.randint(2**(n-1), 2**n - 1)
        if is_prime(s):
            return s

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def generate_rsa_keys(n, seed):
    random.seed(seed)

    p = generate_prime(n)
    print(p)
    q = generate_prime(n)
    while q == p:
        q = generate_prime(n)

    print(q)
    N = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2**(n-1), 2**n - 1)
    gcd, _, _ = extended_gcd(e, phi)
    while gcd != 1:
        e = random.randint(2**(n-1), 2**n - 1)
        gcd, _, _ = extended_gcd(e, phi)

    _, d, _ = extended_gcd(e, phi)
    d = d % phi
    if d < 0:
        d += phi

    return N, e, d

def main():
    n = int(input("Podaj wartość n: "))
    s = int(input("Podaj wartość s: "))

    N, e, d = generate_rsa_keys(n, s)

    print(f"Klucz publiczny: {n},{N},{e}")
    print(f"Klucz prywatny: {n},{N},{d}")

if __name__ == "__main__":
    main()
