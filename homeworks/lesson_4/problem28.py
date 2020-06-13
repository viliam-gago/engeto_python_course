number = int(input('Give me some number: '))
#power number sum

total_sum = 0

while number > 0:
    total_sum += number**2
    number -= 1

print(total_sum)
