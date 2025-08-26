limit = 100
results = [2,3,5]
sieve = [False, False, True, True, False, True] + [False]*(limit-5)

x = 1
x_squared = x**2
while x_squared <= limit:
    y = 1
    y_squared = y**2
    while y_squared <= limit:
        n = 4*x_squared + y_squared
        if n <= limit and n%60 in (1,13,17,29,37,41,49,53):
            sieve[n] = not sieve[n]

        n = 3*x_squared + y_squared
        if n <= limit and n%60 in (7,19,31,43):
            sieve[n] = not sieve[n]

        if x > y:
            n = 3*x_squared - y_squared
            if n <= limit and n%60 in (11,23,47,59):
                sieve[n] = not sieve[n]
        y += 1
        y_squared = y**2
    x += 1
    x_squared = x**2

for prime_number in range(6, len(sieve)):
    if sieve[prime_number]:
        results.append(prime_number)
        for value in range(prime_number**2, limit, prime_number**2):
            sieve[value] = False

print(results)