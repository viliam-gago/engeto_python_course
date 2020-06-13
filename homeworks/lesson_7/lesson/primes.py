def is_prime(n):

    return n == primes(n)[-1]


def primes(n):
    numbers = list(range(2, n+1))
    p = 2

    going = True
    start = 1

    while going:
        for index, number in enumerate(numbers[start:]):
            if number % p == 0:
                numbers.remove(number)

        start += 1

        for x in numbers:
            if x > p:
                p = x
                break

        if p >= max(numbers):
            going = False

    return numbers

print(is_prime(54))