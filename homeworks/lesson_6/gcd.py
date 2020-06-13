def gcd(a,b):

    while b > 1:
        remainder = a % b
        if remainder != 0:
            a, b = b, remainder
        else:
            return b

print(gcd(78,414))

